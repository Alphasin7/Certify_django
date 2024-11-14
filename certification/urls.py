# certification/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('status/<int:student_id>/', views.certification_status, name='certification_status'),
]
