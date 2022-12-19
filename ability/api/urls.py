from rest_framework import routers

from django.contrib import admin
from django.urls import path, include

from ability.api.views import AbilityListCreateView, AbilityRetrieveUpdateDestroyView

app_name = 'ability'
router = routers.DefaultRouter()
router.register('', AbilityListCreateView, basename='ability')
router.register('', AbilityRetrieveUpdateDestroyView, basename='ability')

urlpatterns = [
                  # path('all/', AbilityRetrieveListView),
                  # path('<int:pk>/', AbilityCreateUpdateDestroyView),
              ] + router.urls
