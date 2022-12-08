from rest_framework import routers

from django.contrib import admin
from django.urls import path, include

from ability.api.views import AbilityListCreateView, AbilityRetrieveUpdateDestroyView

router = routers.DefaultRouter()
router.register('', AbilityListCreateView, basename='list--ability')
router.register('', AbilityRetrieveUpdateDestroyView, basename='update-retrieve-destroy-ability')

app_name = 'ability'

urlpatterns = [
                  # path('all/', AbilityRetrieveListView),
                  # path('<int:pk>/', AbilityCreateUpdateDestroyView),
              ] + router.urls
