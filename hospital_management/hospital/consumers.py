# myapp/consumers.py

import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

from .models import Doctor, Appointment
from .serializers import DoctorSerializer, AppointmentSerializer
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete

# List to keep track of connected clients
connected_clients = set()


class DemoConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name = "test"
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()
        connected_clients.add(self)

        # Fetch doctors and their appointments
        doctors = Doctor.objects.all()
        serialized_doctors = DoctorSerializer(doctors, many=True).data

        appointments = Appointment.objects.all()
        serialized_appointments = AppointmentSerializer(appointments, many=True).data

        # Send the data to the client
        self.send(text_data=json.dumps({
            'doctors': serialized_doctors,
            'appointments': serialized_appointments
        }))

    def disconnect(self, close_code):
        connected_clients.remove(self)
        pass

    def receive(self, text_data):
        # Fetch doctors and their appointments
        doctors = Doctor.objects.all()
        serialized_doctors = DoctorSerializer(doctors, many=True).data

        appointments = Appointment.objects.all()
        serialized_appointments = AppointmentSerializer(appointments, many=True).data

        # Send the data to the client
        self.send(text_data=json.dumps({
            'doctors': serialized_doctors,
            'appointments': serialized_appointments
        }))

    def chat_message(self, event):
        message = event['message']

        self.send(text_data=json.dumps({
            "type": "chat",
            "message": message
        }))


@receiver(post_save, sender=Appointment)
def appointment_update_handler(sender, instance, **kwargs):
    # Fetch doctors
    doctors = Doctor.objects.all()
    serialized_doctors = DoctorSerializer(doctors, many=True).data

    # Fetch all appointments
    appointments = Appointment.objects.all()
    serialized_appointments = AppointmentSerializer(appointments, many=True).data

    data = {
        'type': 'appointment_update',
        'data': {
            'doctors': serialized_doctors,
            'appointments': serialized_appointments
        }
    }
    # Send update to all connected clients
    for client in connected_clients:
        client.send(text_data=json.dumps(data))


@receiver(post_delete, sender=Appointment)
def appointment_delete_handler(sender, instance, **kwargs):
    # Fetch doctors
    doctors = Doctor.objects.all()
    serialized_doctors = DoctorSerializer(doctors, many=True).data

    # Fetch all appointments
    appointments = Appointment.objects.all()
    serialized_appointments = AppointmentSerializer(appointments, many=True).data

    data = {
        'type': 'appointment_delete',
        'data': {
            'doctors': serialized_doctors,
            'appointments': serialized_appointments
        }
    }
    # Send update to all connected clients
    for client in connected_clients:
        client.send(text_data=json.dumps(data))
