from django.urls import path
from . import views

urlpatterns = [
    path('merge/', views.MergePdfView.as_view(), name='pdf_merge'),
    path('split/', views.SplitPdfView.as_view(), name='pdf_split'),
    path('compress/', views.CompressPdfView.as_view(), name='pdf_compress'),
    path('to-word/', views.PdfToWordView.as_view(), name='pdf_to_word'),
    path('from-word/', views.WordToPdfView.as_view(), name='word_to_pdf'),
    path('history/', views.FileHistoryView.as_view(), name='pdf_history'),
    path('images-to-pdf/', views.ImagesToPdfView.as_view(), name='images_to_pdf'),
    path('remove-pages/', views.RemovePagesView.as_view(), name='remove_pages'),
    path('info/',         views.GetPdfInfoView.as_view(),  name='pdf_info'),
]
