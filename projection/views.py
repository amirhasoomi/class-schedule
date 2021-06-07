from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import (CreateProposalSerializer, ListProposalSerializer,
                          UpdateProposalSerializer,
                          UpdateLeaderProposalSerializer,
                          AddJudgeSerializer,)
from utils.permissions import IsJudge, IsMember, IsAdmin
from .models import Proposal
from authentication.apps import AuthenticationConfig as AuthConf
from django.db.models import Q


class ProposalViewSet(viewsets.ModelViewSet):

    def get_permissions(self):
        if self.action in {'create', 'destroy'}:
            permission_classes = [IsAuthenticated, IsAdmin | IsMember]
        elif self.action in {'list', 'retrieve'}:
            permission_classes = [IsAuthenticated,
                                  IsAdmin | IsMember | IsJudge]
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateProposalSerializer
        elif self.action == 'list':
            return ListProposalSerializer
        elif self.action == 'destroy':
            return CreateProposalSerializer
        elif self.action == 'retrieve':
            return CreateProposalSerializer

    def get_queryset(self):
        if self.request.user.user_type == AuthConf.USER_TYPE_MEMBER:
            if self.action in {'create', 'list', 'retrieve'}:
                return Proposal.objects.filter(
                    Q(leader=self.request.user) | Q(members=self.request.user))
            elif self.action == 'destroy':
                return Proposal.objects.filter(leader=self.request.user)
        elif self.request.user.user_type == AuthConf.USER_TYPE_JUDGE:
            return Proposal.objects.filter(judges=self.request.user)
        elif self.request.user.user_type == AuthConf.USER_TYPE_ADMIN:
            return Proposal.objects.all()


class UpdateProposalViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, IsAdmin | IsJudge)
    serializer_class = UpdateProposalSerializer

    def get_queryset(self):
        if self.request.user.user_type == AuthConf.USER_TYPE_JUDGE:
            return Proposal.objects.filter(judges=self.request.user)
        elif self.request.user.user_type == AuthConf.USER_TYPE_ADMIN:
            return Proposal.objects.all()


class LeaderUpdateProposalViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, IsMember)
    serializer_class = UpdateLeaderProposalSerializer

    def get_queryset(self):
        if Proposal.objects.filter(leader=self.request.user).exists():
            return Proposal.objects.filter(leader=self.request.user)


class AddJudgeViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, IsAdmin)
    serializer_class = AddJudgeSerializer
    queryset = Proposal.objects.all()

    # FIXME fix delete judge from proposal
