from django.db import models
from django.conf import settings


class ImageRecord(models.Model):
    OPERATION_CHOICES = [
        ('resize', 'Resize'),
        ('compress', 'Compress'),
    ]
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='image_records',
    )
    operation = models.CharField(max_length=20, choices=OPERATION_CHOICES)
    original_filename = models.CharField(max_length=255)
    result_filename = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.email} — {self.operation} — {self.created_at:%Y-%m-%d}"
