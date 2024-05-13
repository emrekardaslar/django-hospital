# hospital/urls.py

from django.urls import path
from .views import DoctorList, DoctorDetail, OtherEmployeeList, OtherEmployeeDetail, PatientList, PatientDetail, \
    AppointmentList, AppointmentDetail, RoomList, RoomDetail, BedList, BedDetail
from . import views

urlpatterns = [
    path('doctors/', DoctorList.as_view(), name='doctor-list'),
    path('doctors/<int:pk>/', DoctorDetail.as_view(), name='doctor-detail'),
    path('other-employees/', OtherEmployeeList.as_view(), name='otheremployee-list'),
    path('other-employees/<int:pk>/', OtherEmployeeDetail.as_view(), name='otheremployee-detail'),
    path('patients/', PatientList.as_view(), name='patient-list'),
    path('patients/<int:pk>/', PatientDetail.as_view(), name='patient-detail'),
    path('appointments/', AppointmentList.as_view(), name='appointment-list'),
    path('appointments/<int:pk>/', AppointmentDetail.as_view(), name='appointment-detail'),
    path('rooms/', RoomList.as_view(), name='room-list'),
    path('rooms/<int:pk>/', RoomDetail.as_view(), name='room-detail'),
    path('beds/', BedList.as_view(), name='bed-list'),
    path('beds/<int:pk>/', BedDetail.as_view(), name='bed-detail'),
    path('websocket-demo/', views.websocket_demo, name='websocket_demo'),
]
