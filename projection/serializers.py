from rest_framework import serializers
from .models import Proposal
from django.utils.crypto import get_random_string


class CreateProposalSerializer(serializers.ModelSerializer):
    leader = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Proposal
        fields = ('pk', 'unique_code', 'title', 'description',
                  'leader', 'members', 'file', 'judges', 'register_date')
        read_only_fields = ('pk', 'unique_code')

    def create(self, validated_data):
        validated_data['unique_code'] = get_random_string(length=10).upper()
        return super().create(validated_data)


class ListProposalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Proposal
        fields = ('__all__')
        read_only_fields = ('pk', 'unique_code')
