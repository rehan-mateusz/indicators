from django.urls import path

from . import views

app_name = 'indicators'

urlpatterns = [
    path('upload/', views.UploadView.as_view(), name='upload'),
]
