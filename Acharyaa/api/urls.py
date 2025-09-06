from django.urls import path
from .views import UserListCreateView, UserDetailView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("auth/login/", TokenObtainPairView.as_view(), name="login"),
    path("auth/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("users/", UserListCreateView.as_view(), name="user_list"),
    # path("users/<int:pk>/", UserDetailView.as_view(), name="user_detail"),
]