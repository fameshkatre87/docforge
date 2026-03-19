from django.db import models
from django.conf import settings


class FileRecord(models.Model):
    OPERATION_CHOICES = [
        ('merge', 'Merge PDF'),
        ('split', 'Split PDF'),
        ('compress_pdf', 'Compress PDF'),
        ('word_to_pdf', 'Word to PDF'),
        ('pdf_to_word', 'PDF to Word'),
        ('images_to_pdf', 'Images to PDF'),
        ('remove_pages',  'Remove Pages'),
    ]
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='pdf_records',
    )
    operation = models.CharField(max_length=20, choices=OPERATION_CHOICES)
    original_filename = models.CharField(max_length=255)
    result_filename = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.email} — {self.operation} — {self.created_at:%Y-%m-%d}"
