# hospital/views.py

from rest_framework import generics
from .models import Doctor, OtherEmployee, Patient, Appointment, Room, Bed
from .serializers import DoctorSerializer, OtherEmployeeSerializer, PatientSerializer, AppointmentSerializer, \
    RoomSerializer, BedSerializer


class DoctorList(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class DoctorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class OtherEmployeeList(generics.ListCreateAPIView):
    queryset = OtherEmployee.objects.all()
    serializer_class = OtherEmployeeSerializer


class OtherEmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = OtherEmployee.objects.all()
    serializer_class = OtherEmployeeSerializer


class PatientList(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class PatientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class AppointmentList(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


class AppointmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


class RoomList(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class RoomDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class BedList(generics.ListCreateAPIView):
    queryset = Bed.objects.all()
    serializer_class = BedSerializer


class BedDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bed.objects.all()
    serializer_class = BedSerializer
