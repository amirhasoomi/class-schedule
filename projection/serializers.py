from rest_framework import serializers
from .models import Proposal
from django.utils.crypto import get_random_string


class CreateProposalSerializer(serializers.ModelSerializer):
    leader = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Proposal
        fields = ('pk', 'unique_code', 'title', 'description',
                  'leader', 'members', 'file', 'judges',
                  'register_date', 'status')
        read_only_fields = ('pk', 'unique_code', 'register_date', 'status')

    def create(self, validated_data):
        validated_data['unique_code'] = get_random_string(length=10).upper()
        return super().create(validated_data)


class ListProposalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Proposal
        fields = ('__all__')
        read_only_fields = ('pk', 'unique_code')


class UpdateProposalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proposal
        fields = ('__all__')
        read_only_fields = ('pk', 'unique_code', 'title', 'description',
                            'leader', 'members', 'file', 'judges',
                            'register_date', 'ip_address', 'status')


class UpdateLeaderProposalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proposal
        fields = ('__all__')
        read_only_fields = ('pk', 'unique_code', 'register_date', 'judges',
                            'check_date', 'assent_date', 'present_date',
                            'accept_date', 'aontract_date', 'ip_address')
