from django.urls import path
from dashboard.views import dashboard_overview

urlpatterns=[
    path('overview/', dashboard_overview, name='dashboard_overview'),  
      
    ]
