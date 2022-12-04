from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Resume Back End API')

urlpatterns = [
    path('api/docs', schema_view),
    path('admin/', admin.site.urls),
    path('api/ability/', include('ability.api.urls')),
    path('api/about_me/', include('about_me.api.urls')),
    path('api/comment/', include('comment.api.urls')),
    path('api/education/', include('education.api.urls')),
    path('api/jobs/', include('jobs.api.urls')),
    path('api/land_page/', include('land_page.api.urls')),
    path('api/projects/', include('projects.api.urls')),
    path('api/social/', include('social.api.urls')),
    path('api/user/', include('user.api.urls')),
]
