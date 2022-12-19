from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework_swagger.views import get_swagger_view

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('api/docs', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('api/auth/', include('rest_framework.urls')),
    path('api/ability/', include('ability.api.urls'), name='ability'),
    # path('api/about_me/', include('about_me.api.urls')),
    # path('api/comment/', include('comment.api.urls')),
    # path('api/education/', include('education.api.urls')),
    # path('api/jobs/', include('jobs.api.urls')),
    # path('api/land_page/', include('land_page.api.urls')),
    # path('api/projects/', include('projects.api.urls')),
    # path('api/social/', include('social.api.urls')),
    # path('api/user/', include('user.api.urls')),
]
