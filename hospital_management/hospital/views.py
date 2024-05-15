# hospital/views.py

from rest_framework import generics
from .models import Doctor, OtherEmployee, Patient, Appointment, Room, Bed
from .permissions import IsAdminForNonGet
from .serializers import DoctorSerializer, OtherEmployeeSerializer, PatientSerializer, AppointmentSerializer, \
    RoomSerializer, BedSerializer

from django.shortcuts import render


class BaseAdminForNonGetView(generics.GenericAPIView):
    permission_classes = [IsAdminForNonGet]


class DoctorList(BaseAdminForNonGetView, generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class DoctorDetail(BaseAdminForNonGetView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class OtherEmployeeList(BaseAdminForNonGetView, generics.ListCreateAPIView):
    queryset = OtherEmployee.objects.all()
    serializer_class = OtherEmployeeSerializer


class OtherEmployeeDetail(BaseAdminForNonGetView, generics.RetrieveUpdateDestroyAPIView):
    queryset = OtherEmployee.objects.all()
    serializer_class = OtherEmployeeSerializer


class PatientList(BaseAdminForNonGetView, generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class PatientDetail(BaseAdminForNonGetView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class AppointmentList(BaseAdminForNonGetView, generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


class AppointmentDetail(BaseAdminForNonGetView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


class RoomList(BaseAdminForNonGetView, generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class RoomDetail(BaseAdminForNonGetView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class BedList(BaseAdminForNonGetView, generics.ListCreateAPIView):
    queryset = Bed.objects.all()
    serializer_class = BedSerializer


class BedDetail(BaseAdminForNonGetView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Bed.objects.all()
    serializer_class = BedSerializer


def appointments(request):
    return render(request, 'appointments.html')
