from django.contrib import admin
from .models import ImageRecord


@admin.register(ImageRecord)
class ImageRecordAdmin(admin.ModelAdmin):
    list_display = ['user', 'operation', 'original_filename', 'created_at']
    list_filter = ['operation']
    search_fields = ['user__email', 'original_filename']
    ordering = ['-created_at']
