from django.urls import path
from .views import (ProposalViewSet, UpdateProposalViewSet,
                    LeaderUpdateProposalViewSet, AddJudgeViewSet,
                    ExportPdfViewSet)

urlpatterns = [
    path('proposal',
         ProposalViewSet.as_view({'post': 'create',
                                  'get': 'list'})),
    path('proposal/<int:pk>',
         ProposalViewSet.as_view({'post': 'create',
                                  'get': 'retrieve',
                                  'delete': 'destroy'})),
    path('proposal/<int:pk>',
         UpdateProposalViewSet.as_view({'patch': 'update',
                                        'put': 'update'})),
    path('leader/proposal/<int:pk>',
         LeaderUpdateProposalViewSet.as_view({'patch': 'update',
                                              'put': 'update'})),

    path('proposal/<int:pk>/judge',
         AddJudgeViewSet.as_view({'get': 'retrieve',
                                  'patch': 'update'})),

    path('proposal/<int:pk>/export',
         ExportPdfViewSet.as_view({'get': 'retrieve'})),
]
