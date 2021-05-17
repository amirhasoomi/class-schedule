from django.urls import path
from .views import (SliderViewSet, BannerViewSet,
                    PartnersViewSet, SupportersViewSet,
                    ContactViewSet)


urlpatterns = [
    path('slider', SliderViewSet.as_view({'get': 'list',
                                          'post': 'create'})),
    path('slider/<int:pk>', SliderViewSet.as_view({'delete': 'destroy',
                                                   'put': 'update'})),

    path('banner', BannerViewSet.as_view({'get': 'list',
                                          'post': 'create'})),
    path('banner/<int:pk>', BannerViewSet.as_view({'delete': 'destroy',
                                                   'put': 'update'})),

    path('partners', PartnersViewSet.as_view({'get': 'list',
                                              'post': 'create'})),
    path('partners/<int:pk>', PartnersViewSet.as_view({'delete': 'destroy',
                                                       'put': 'update'})),

    path('support', SupportersViewSet.as_view({'get': 'list',
                                               'post': 'create'})),
    path('support/<int:pk>', SupportersViewSet.as_view({'delete': 'destroy',
                                                        'put': 'update'})),

    path('contact', ContactViewSet.as_view({'get': 'list',
                                            'post': 'create'})),
    path('contact/<int:pk>', ContactViewSet.as_view({'delete': 'destroy'})),
]
