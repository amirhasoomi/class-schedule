from django.urls import path
from .views import (SliderView, BannerView,
                    PartnersView, SupportersView)


urlpatterns = [
    path('slider', SliderView.as_view()),
    path('banner', BannerView.as_view()),
    path('partners', PartnersView.as_view()),
    path('support', SupportersView.as_view()),
]
