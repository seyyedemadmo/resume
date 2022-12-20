from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from about_me.api.views import AboutModelViewSet

app_name = 'about_me'

router = routers.DefaultRouter()
router.register('', AboutModelViewSet, basename='about_me')

urlpatterns = [

              ] + router.urls
