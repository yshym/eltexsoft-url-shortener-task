from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from rest_framework.authtoken import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title='URL Shortener API',
        default_version='v1',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('login/', views.obtain_auth_token, name='login'),
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='docs'),
    path('', include('shortener.urls')),
]
