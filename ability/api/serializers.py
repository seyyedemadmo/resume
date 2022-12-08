from rest_framework.serializers import ModelSerializer

from ability.models import Ability


class AbilityListSerializer(ModelSerializer):
    class Meta:
        model = Ability
        exclude = ['visible', 'created_at', 'updated_at']


class AbilityUpdateSerializer(ModelSerializer):
    class Meta:
        model = Ability
        exclude = ['created_at', 'updated_at']