from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from apps.user.views.auth import CustomTokenObtainPairView, CustomTokenRefreshView
from apps.user.views.register import RegisterView

urlpatterns = [
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
]
