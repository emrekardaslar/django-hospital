from django.contrib import admin
from django.urls import path, include

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Hospital Management API",
        default_version='v1',
        description="API for hospital management",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="emre@gmail.com"),
        license=openapi.License(name="Your License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/', include('hospital.urls')),
    path('hospital/', include('hospital.urls')),  # Replace 'myapp' with your app name
]