# hospital/models.py

from django.db import models


# Model for Employees (Base class)
class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    # Common fields for all employees, e.g., contact information, hire date, etc.

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# Model for Doctors (Inherits from Employee)
class Doctor(Employee):
    specialities = (
        ('General Medicine', 'General Medicine'),
        ('Family Medicine', 'Family Medicine'),
        ('Internal Medicine', 'Internal Medicine'),
        ('Pediatrics', 'Pediatrics'),
        ('Cardiology', 'Cardiology'),
        ('Gastroenterology', 'Gastroenterology'),
        ('Neurology', 'Neurology'),
        ('Orthopedics', 'Orthopedics'),
    )
    specialty = models.CharField(max_length=100, choices=specialities)
    # Additional fields specific to doctors


# Model for Other Employees (Inherits from Employee)
class OtherEmployee(Employee):
    DEPARTMENT_CHOICES = (
        ('Administration', 'Administration'),
        ('Finance', 'Finance'),
        ('Human Resources', 'Human Resources'),
        ('Information Technology', 'Information Technology'),
        ('Marketing', 'Marketing'),
        ('Operations', 'Operations'),
        ('Sales', 'Sales'),
    )
    department = models.CharField(max_length=100, choices=DEPARTMENT_CHOICES)
    # Additional fields specific to other employees, e.g., department, job title, etc.


# Model for Patients
class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()

    # You can add more fields like address, contact information, etc.

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# Model for Appointments
class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()

    # You can add more fields like appointment status, reason, notes, etc.

    def __str__(self):
        return f"Appointment with Dr. {self.doctor} on {self.appointment_date}"


# Model for Rooms
class Room(models.Model):
    room_number = models.IntegerField(default=1, choices=((i,i) for i in range(1, 101)), unique=True)

    # You can add more fields like room type, description, etc.

    def __str__(self):
        return f"Room {self.room_number}"


# Model for Beds
class Bed(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    bed_number = models.IntegerField(default=1, choices=((i,i) for i in range(1, 6)))
    is_occupied = models.BooleanField(default=False)

    # You can add more fields like patient assigned, bed type, etc.

    def __str__(self):
        return f"Bed {self.bed_number} in Room {self.room.room_number}"

    class Meta:
        unique_together = ('bed_number', 'room')


# Model for Treatments
class Treatment(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    # You can add more fields like treatment duration, cost, etc.

    def __str__(self):
        return f"{self.name} for {self.patient} by Dr. {self.doctor}"
