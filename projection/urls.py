from django.urls import path
from .views import (ProposalViewSet, UpdateProposalViewSet,
                    LeaderUpdateProposalViewSet)

urlpatterns = [
    path('proposal', ProposalViewSet.as_view({'post': 'create',
                                              'get': 'list'})),
    path('proposal/<int:pk>', ProposalViewSet.as_view({'post': 'create',
                                                       'get': 'retrieve',
                                                       'delete': 'destroy'})),
    path('proposal/<int:pk>',
         UpdateProposalViewSet.as_view({'patch': 'update',
                                       'put': 'update'})),
    path('leader/proposal/<int:pk>',
         LeaderUpdateProposalViewSet.as_view({'patch': 'update',
                                              'put': 'update'})),

]
