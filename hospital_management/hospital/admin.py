# hospital/admin.py

from django.contrib import admin
from .models import Doctor, OtherEmployee, Patient, Appointment, Room, Bed, Treatment


# Admin class for Doctor
@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'specialty']


# Admin class for Other Employee
@admin.register(OtherEmployee)
class OtherEmployeeAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'department']


# Admin class for Patient
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'date_of_birth']


# Admin class for Appointment
@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['doctor', 'patient', 'appointment_date']


# Admin class for Room
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['room_number']


# Admin class for Bed
@admin.register(Bed)
class BedAdmin(admin.ModelAdmin):
    list_display = ['bed_number', 'room', 'is_occupied']


# Admin class for Treatment
@admin.register(Treatment)
class TreatmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'doctor', 'patient']
