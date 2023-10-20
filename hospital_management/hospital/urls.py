# hospital/urls.py

from django.urls import path
from .views import DoctorList, DoctorDetail

urlpatterns = [
    path('doctors/', DoctorList.as_view(), name='doctor-list'),
    path('doctors/<int:pk>/', DoctorDetail.as_view(), name='doctor-detail'),
    # Define URLs for other models' views here
]
