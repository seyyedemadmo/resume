from rest_framework.serializers import ModelSerializer

from about_me.models import About


class ListRetrieveAboutSerializer(ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'


class UpdateCreateAboutSerializer(ModelSerializer):
    class Meta:
        model = About
        exclude = ['updated_at', 'created_at']
