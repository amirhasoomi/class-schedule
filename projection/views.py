from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import CreateProposalSerializer, ListProposalSerializer
from utils.permissions import IsJudge, IsMember, IsAdmin
from .models import Proposal
from authentication.apps import AuthenticationConfig as AuthConf


class ProposalViewSet(viewsets.ModelViewSet):

    def get_permissions(self):
        if self.action in {'create', 'Destroy'}:
            permission_classes = [IsAuthenticated, IsAdmin | IsMember]
        elif self.action in {'list', 'update', 'retrieve'}:
            permission_classes = [IsAuthenticated,
                                  IsAdmin | IsMember | IsJudge]
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateProposalSerializer
        elif self.action == 'list':
            return ListProposalSerializer
        # elif self.action == 'update':
        #     return True  # serializers.GroupDetailSerializer
        # elif self.action == 'Destroy':
        #     return True  # serializers.GroupDetailSerializer
        # elif self.action == 'retrieve':
        #     return True  # serializers.GroupDetailSerializer

    def get_queryset(self):
        if self.request.user.user_type == AuthConf.USER_TYPE_MEMBER:
            return Proposal.objects.select_related(
                'leader' or 'members'
            ).filter(leader=self.request.user)
        elif self.request.user.user_type == AuthConf.USER_TYPE_JUDGE:
            return Proposal.objects.select_related(
                'judge'
            ).filter(judge=self.request.user)
        elif self.request.user.user_type == AuthConf.USER_TYPE_ADMIN:
            return Proposal.objects.all()

    # def get_queryset(self):
    #     return Proposal.objects.exclude().order_by('pk')
