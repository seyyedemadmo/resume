from django.contrib import admin
from django.urls import path, include

from ability.api.views import AbilityListView

app_name = 'ability'
urlpatterns = [
    path('all/', AbilityListView.as_view()),
]
