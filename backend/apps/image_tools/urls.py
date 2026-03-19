from django.urls import path
from . import views

urlpatterns = [
    path('resize/', views.ResizeImageView.as_view(), name='image_resize'),
    path('compress/', views.CompressImageView.as_view(), name='image_compress'),
    path('history/', views.ImageHistoryView.as_view(), name='image_history'),
]
