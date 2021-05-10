from rest_framework import serializers
from .models import Slider, Banner, Partners, supporters


class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = ('__all__')


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ('__all__')


class PartnersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partners
        fields = ('__all__')


class SupportersSerializer(serializers.ModelSerializer):
    class Meta:
        model = supporters
        fields = ('__all__')
