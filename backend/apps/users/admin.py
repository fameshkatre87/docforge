from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ['email', 'username', 'plan', 'files_processed', 'is_staff', 'created_at']
    list_filter = ['plan', 'is_staff', 'is_active']
    search_fields = ['email', 'username']
    ordering = ['-created_at']

    fieldsets = UserAdmin.fieldsets + (
        ('DocForge Info', {'fields': ('plan', 'files_processed')}),
    )
