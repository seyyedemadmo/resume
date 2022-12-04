from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from ability.models import Ability
from ability.api.serializers import AbilityListSerializer


class AbilityListView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = AbilityListSerializer

    def get_queryset(self):
        return Ability.objects.filter(visible=True)
