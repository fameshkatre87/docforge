from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('me/', views.ProfileView.as_view(), name='profile'),
    path('admin/users/', views.AdminUsersView.as_view(), name='admin_users'),
    path('admin/stats/', views.AdminStatsView.as_view(), name='admin_stats'),
]
