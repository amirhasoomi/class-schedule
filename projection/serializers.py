from rest_framework import serializers
from .models import Proposal
from django.utils.crypto import get_random_string
from authentication.apps import AuthenticationConfig as AuthConf


class CreateProposalSerializer(serializers.ModelSerializer):
    leader = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Proposal
        fields = ('pk', 'unique_code', 'title', 'description',
                  'leader', 'members', 'file', 'judges', 'register_date')
        read_only_fields = ('pk', 'unique_code', 'register_date', 'judges',)

    def validate(self, attrs):
        members = attrs['members']
        leader = attrs['leader']
        for member in members:
            if not member.user_type == AuthConf.USER_TYPE_MEMBER:
                raise serializers.ValidationError(
                    dict(members=[f'{member.pk} is not a member!', ]))
            elif member == leader:
                raise serializers.ValidationError(
                    dict(members=['leader can not be a member!', ]))
        return super().validate(attrs)

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
                            'register_date', 'ip_address')


class UpdateLeaderProposalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proposal
        fields = ('__all__')
        read_only_fields = ('pk', 'unique_code', 'register_date', 'judges',
                            'check_date', 'assent_date', 'present_date',
                            'accept_date', 'aontract_date', 'ip_address')


class AddJudgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proposal
        fields = ('judges',)
        read_only_fields = ('pk', 'unique_code', 'register_date', 'check_date',
                            'assent_date', 'present_date', 'accept_date',
                            'aontract_date', 'ip_address', 'title',
                            'description', 'leader', 'members', 'file')

    def validate(self, attrs):
        judges = attrs['judges']
        for judge in judges:
            if not judge.user_type == AuthConf.USER_TYPE_JUDGE:
                raise serializers.ValidationError(
                    dict(judges=[f'{judge.pk} is not a judge!', ]))
        return super().validate(attrs)
