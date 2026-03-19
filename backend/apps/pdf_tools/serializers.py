from rest_framework import serializers
from .models import FileRecord


class FileRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileRecord
        fields = ['id', 'operation', 'original_filename', 'result_filename', 'created_at']
        read_only_fields = ['id', 'created_at']
