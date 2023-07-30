
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import (PLatoSerializer, FieldSerializer,
                          CreateLessonSerializer, ListLessonSerializer,
                          CreateScheduleSerializer, ListScheduleSerializer
                          )
from utils.permissions import IsAdmin
from .models import Plato, Field, Lesson, Schedule
from authentication.apps import AuthenticationConfig as AuthConf


class PlatoViewSet(viewsets.ModelViewSet):
    serializer_class = PLatoSerializer
    queryset = Plato.objects.all()

    def get_permissions(self):
        if self.action in {'create', 'destroy', 'update'}:
            permission_classes = [IsAuthenticated, IsAdmin]
        elif self.action in {'list', 'retrieve'}:
            permission_classes = [IsAuthenticated, ]
        return [permission() for permission in permission_classes]


class FieldViewSet(viewsets.ModelViewSet):
    serializer_class = FieldSerializer
    queryset = Field.objects.all()

    def get_permissions(self):
        if self.action in {'create', 'destroy', 'update'}:
            permission_classes = [IsAuthenticated, IsAdmin]
        elif self.action in {'list', 'retrieve'}:
            permission_classes = [IsAuthenticated, ]
        return [permission() for permission in permission_classes]


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()

    def get_permissions(self):
        if self.action in {'create', 'destroy', 'update'}:
            permission_classes = [IsAuthenticated, IsAdmin]
        elif self.action in {'list', 'retrieve'}:
            permission_classes = [IsAuthenticated, ]
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action in {'create', 'destroy', 'update'}:
            return CreateLessonSerializer
        elif self.action in {'list', 'retrieve'}:
            return ListLessonSerializer


class ScheduleViewSet(viewsets.ModelViewSet):

    def get_permissions(self):
        if self.action in {'create', 'destroy', 'update'}:
            permission_classes = [IsAuthenticated, IsAdmin]
        elif self.action in {'list', 'retrieve'}:
            permission_classes = [IsAuthenticated, ]
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action in {'create', 'destroy'}:
            return CreateScheduleSerializer
        elif self.action in {'list', 'retrieve'}:
            return ListScheduleSerializer

    def get_queryset(self):
        if self.request.user.user_type == AuthConf.USER_TYPE_ADMIN:
            return Schedule.objects.all()
        elif self.request.user.user_type == AuthConf.USER_TYPE_USER:
            return Schedule.objects.filter(professor=self.request.user)


# class ExportPdfViewSet(viewsets.ModelViewSet):
#     permission_classes = (IsAuthenticated,)
#     serializer_class = ListProposalSerializer
#     queryset = Proposal.objects.all()

#     def get_queryset(self):
#         if self.request.user.user_type == AuthConf.USER_TYPE_MEMBER:
#             scope = self.queryset.filter(
#                 Q(leader=self.request.user) | Q(members=self.request.user))
#         elif self.request.user.user_type == AuthConf.USER_TYPE_JUDGE:
#             scope = self.queryset.filter(judges=self.request.user)
#         elif self.request.user.user_type == AuthConf.USER_TYPE_ADMIN:
#             scope = self.queryset
#         return scope

#     def retrieve(self, request, *args, **kwargs):

#         if self.queryset.filter(pk=kwargs['pk']).exists():
#             proposal = self.queryset.filter(pk=kwargs['pk']).get()
#             members = proposal.members.all()
#             judges = proposal.judges.all()
#             register_date = jdatetime.date.fromgregorian(
#                 date=proposal.register_date)

#             if proposal.check_date is None:
#                 status = 'در انتظار برسی اولیه'
#                 status_date = jdatetime.date.fromgregorian(
#                     date=proposal.register_date)

#             elif proposal.assent_date is None:
#                 status = 'در انتظار پذبرش'
#                 status_date = jdatetime.date.fromgregorian(
#                     date=proposal.check_date)

#             elif proposal.present_date is None:
#                 status = 'در انتظار دریافت تاریخ دفاع'
#                 status_date = jdatetime.date.fromgregorian(
#                     date=proposal.assent_date)

#             elif proposal.accept_date is None:
#                 status = 'در انتظار تصویب'
#                 status_date = jdatetime.date.fromgregorian(
#                     date=proposal.present_date)

#             elif proposal.aontract_date is None:
#                 status = 'در انتظار دریافت تاریخ انعقاد قرارداد'
#                 status_date = jdatetime.date.fromgregorian(
#                     date=proposal.accept_date)

#             else:
#                 status = 'قرارداد شد'
#                 status_date = jdatetime.date.fromgregorian(
#                     date=proposal.aontract_date)

#             template = get_template("template.html")
#             context = dict(proposal=proposal,
#                            members=members,
#                            judges=judges,
#                            status=status,
#                            status_date=status_date,
#                            register_date=register_date)
#             html = template.render(context).replace("\n", "").strip()
#             with NamedTemporaryFile(delete=True)as pdf:
#                 pdf.write(PDF.from_string(html, False))
#                 pdf.flush()
#                 pdf_path = default_storage.save(
#                     'pdf/'+proposal.unique_code + '.pdf', pdf)
#                 url = request.build_absolute_uri(default_storage.url(pdf_path))
#                 return Response({'pdf': url})

#         else:
#             raise ValidationError(dict(error='proposal not found!'))
