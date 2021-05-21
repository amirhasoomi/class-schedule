from django.urls import path
from .views import (ProposalViewSet)

urlpatterns = [
    path('proposal', ProposalViewSet.as_view({'post': 'create',
                                              'get': 'list'})),

]
