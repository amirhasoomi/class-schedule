from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from utils.permissions import IsAdmin
from .serializers import (SliderSerializer, BannerSerializer,
                          PartnersSerializer, SupportersSerializer)


class SliderView(generics.CreateAPIView,
                 generics.RetrieveAPIView,
                 generics.UpdateAPIView,
                 generics.DestroyAPIView):
    permission_classes = (IsAuthenticated, IsAdmin)
    serializer_class = SliderSerializer


class BannerView(generics.CreateAPIView,
                 generics.RetrieveAPIView,
                 generics.UpdateAPIView,
                 generics.DestroyAPIView):
    permission_classes = (IsAuthenticated, IsAdmin)
    serializer_class = BannerSerializer


class PartnersView(generics.CreateAPIView,
                   generics.RetrieveAPIView,
                   generics.UpdateAPIView,
                   generics.DestroyAPIView):
    permission_classes = (IsAuthenticated, IsAdmin)
    serializer_class = PartnersSerializer


class SupportersView(generics.CreateAPIView,
                     generics.RetrieveAPIView,
                     generics.UpdateAPIView,
                     generics.DestroyAPIView):
    permission_classes = (IsAuthenticated, IsAdmin)
    serializer_class = SupportersSerializer
