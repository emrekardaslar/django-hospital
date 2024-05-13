// myapp/static/js/mywebsocket.js

document.addEventListener('DOMContentLoaded', function () {
    const socket = new WebSocket("ws://" + window.location.host + "/ws/hospital/");

    socket.onopen = function(event) {
        console.log('WebSocket is connected.');
    };

    socket.onmessage = function(event) {
        const data = JSON.parse(event.data);
        console.log(data);
        if (data.type === 'appointment_update') {
            updateAppointment(data.data);
        } else {
            displayDoctorsAndAppointments(data);
        }
    };

    // Function to send message to server
    function sendMessage() {
        const messageInput = document.getElementById('message-input');
        const message = messageInput.value.trim();
        if (message) {
            socket.send(JSON.stringify({'message': message}));
            messageInput.value = ''; // Clear input field
        }
    }

    function displayDoctorsAndAppointments(data) {
        const messageContainer = document.getElementById('message-container');
        const doctors = data.doctors;
        const appointments = data.appointments;

        // Clear the message container before displaying data
        messageContainer.innerHTML = '';

        // Display doctors
        messageContainer.innerHTML += "<h2>Doctors:</h2>";
        doctors.forEach(function(doctor) {
            messageContainer.innerHTML += `<p>${doctor.first_name} ${doctor.last_name} - ${doctor.specialty}</p>`;
        });
        // Sort appointments by appointment_date
        appointments.sort((a, b) => new Date(a.appointment_date) - new Date(b.appointment_date));
        // Display appointments
        messageContainer.innerHTML += "<h2>Appointments:</h2>";
        appointments.forEach(function(appointment) {
            messageContainer.innerHTML += `<p>Appointment with Dr. ${appointment.doctor} for Patient No: ${appointment.patient} on ${appointment.appointment_date}</p>`;
        });
    }

    function updateAppointment(appointment) {
        const messageContainer = document.getElementById('message-container');
        const existingAppointment = messageContainer.querySelector(`#appointment-${appointment.id}`);
        if (existingAppointment) {
            existingAppointment.innerHTML = `<p>Appointment with Dr. ${appointment.doctor} for Patient No: ${appointment.patient} on ${appointment.appointment_date}</p>`;
        } else {
            messageContainer.innerHTML += `<p id="appointment-${appointment.id}">Appointment with Dr. ${appointment.doctor} for Patient No: ${appointment.patient} on ${appointment.appointment_date}</p>`;
        }
    }
});
