from django.urls import path
from .views import (
    PlatoViewSet, FieldViewSet, LessonViewSet, ScheduleViewSet
)

urlpatterns = [

    path('palto',
         PlatoViewSet.as_view({'post': 'create',
                               'get': 'list', })),
    path('palto/<int:pk>',
         PlatoViewSet.as_view({'get': 'retrieve',
                               'delete': 'destroy',
                               'put': 'update'})),
    path('field',
         FieldViewSet.as_view({'post': 'create',
                               'get': 'list', })),
    path('field/<int:pk>',
         FieldViewSet.as_view({'get': 'retrieve',
                               'delete': 'destroy',
                               'put': 'update'})),
    path('lesson',
         LessonViewSet.as_view({'post': 'create',
                               'get': 'list', })),
    path('lesson/<int:pk>',
         LessonViewSet.as_view({'get': 'retrieve',
                               'delete': 'destroy',
                                'put': 'update'})),
    path('schedule',
         ScheduleViewSet.as_view({'post': 'create',
                                  'get': 'list', })),
    path('schedule/<int:pk>',
         ScheduleViewSet.as_view({'get': 'retrieve',
                                  'delete': 'destroy',
                                  'put': 'update'})),

]
