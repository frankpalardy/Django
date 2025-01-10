from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet, UserRegistrationView, test_view
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'items', ItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/register/', UserRegistrationView.as_view(), name='user_registration'),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/test/', test_view, name='test_view'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('accounts/', include('django.contrib.auth.urls')),
]