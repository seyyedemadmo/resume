from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict

from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from about_me.models import About
from about_me.permissions import OnlyAdminOrListRetrieve
from about_me.api.serializers import ListRetrieveAboutSerializer, UpdateCreateAboutSerializer


class AboutModelViewSet(ModelViewSet):
    permission_classes = [OnlyAdminOrListRetrieve]
    queryset = About.objects.all()

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return ListRetrieveAboutSerializer
        return UpdateCreateAboutSerializer

    @action(detail=False, methods=['get'], permission_classes=[AllowAny])
    def get_main(self, request, *args, **kwargs):
        about = get_object_or_404(About, chosen=True)
        data = model_to_dict(about)
        return Response(data=data)
