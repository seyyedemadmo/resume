from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.mixins import ListModelMixin, UpdateModelMixin, CreateModelMixin, RetrieveModelMixin, \
    DestroyModelMixin
from rest_framework.permissions import AllowAny, IsAdminUser

from ability.models import Ability
from ability.api.serializers import AbilityListSerializer, AbilityUpdateSerializer
from ability.permissions import OnlyAdminCanCreate


class AbilityListCreateView(ListModelMixin, CreateModelMixin, GenericViewSet):
    permission_classes = [OnlyAdminCanCreate]
    serializer_class = AbilityListSerializer

    def get_queryset(self):
        return Ability.objects.filter(visible=True)


class AbilityRetrieveUpdateDestroyView(RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin,
                                       GenericViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = AbilityUpdateSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        return Ability.objects.filter(visible=True)
