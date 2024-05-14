// myapp/static/js/mywebsocket.js

document.addEventListener("DOMContentLoaded", function () {
  const socket = new WebSocket(
    "ws://" + window.location.host + "/ws/hospital/"
  );

  socket.onopen = function (event) {
    console.log("WebSocket is connected.");
  };

  socket.onmessage = function (event) {
    const data = JSON.parse(event.data);
    console.log(data);
    if (data.type === "appointment_update") {
      updateOrCreateAppointment(data.data);
    } else if (data.type === "appointment_delete") {
      deleteAppointment(data.data.id);
    } else {
      displayDoctorsAndAppointments(data);
    }
  };

  // Function to send message to server
  function sendMessage() {
    const messageInput = document.getElementById("message-input");
    const message = messageInput.value.trim();
    if (message) {
      socket.send(JSON.stringify({ message: message }));
      messageInput.value = ""; // Clear input field
    }
  }

  function displayDoctorsAndAppointments(data) {
    const messageContainer = document.getElementById("message-container");
    const doctors = data.doctors;
    let appointments = data.appointments;

    // Clear the message container before displaying data
    messageContainer.innerHTML = "";

    // Display doctors
    messageContainer.innerHTML += "<h2>Doctors:</h2>";
    doctors.forEach(function (doctor) {
      messageContainer.innerHTML += `<p>${doctor.first_name} ${doctor.last_name} - ${doctor.specialty}</p>`;
    });

    // Sort appointments by appointment_date
    appointments.sort(
      (a, b) => new Date(a.appointment_date) - new Date(b.appointment_date)
    );

    // Display appointments
    messageContainer.innerHTML += "<h2>Appointments:</h2>";
    appointments.forEach(function (appointment) {
      messageContainer.innerHTML += `<p id="appointment-${appointment.id}">Appointment with Dr. ${appointment.doctor.first_name} for Patient No: ${appointment.patient.first_name} on ${appointment.appointment_date}</p>`;
    });
  }

  function updateOrCreateAppointment(appointment) {
    const appointmentElement = document.getElementById(
      `appointment-${appointment.id}`
    );
    if (appointmentElement) {
      // Update existing appointment
      appointmentElement.innerHTML = `Appointment with Dr. ${appointment.doctor.first_name} for Patient No: ${appointment.patient.first_name} on ${appointment.appointment_date}`;
    } else {
      // Create new appointment
      const messageContainer = document.getElementById("message-container");
      messageContainer.innerHTML += `<p id="appointment-${appointment.id}">Appointment with Dr. ${appointment.doctor.first_name} for Patient No: ${appointment.patient.first_name} on ${appointment.appointment_date}</p>`;
    }

    // Sort appointments after updating or creating
    sortAppointments();

    // TODO Redisplay doctors
    //displayDoctorsAndAppointments({ doctors: appointment.doctor.first_names });
  }

  function deleteAppointment(appointmentId) {
    const appointmentElement = document.getElementById(
      `appointment-${appointmentId}`
    );
    if (appointmentElement) {
      appointmentElement.remove();
    }

    // Sort appointments after deletion
    sortAppointments();

    // Redisplay doctors
    displayDoctorsAndAppointments({ doctors: appointment.doctor.first_names });
  }

  function sortAppointments() {
    const messageContainer = document.getElementById("message-container");
    const appointmentElements = messageContainer.querySelectorAll(
      '[id^="appointment-"]'
    );
    const sortedAppointments = Array.from(appointmentElements).sort((a, b) => {
      const aDate = new Date(a.textContent.split("on ")[1]);
      const bDate = new Date(b.textContent.split("on ")[1]);
      return aDate - bDate;
    });
    messageContainer.innerHTML = "";
    sortedAppointments.forEach((appointment) =>
      messageContainer.appendChild(appointment)
    );
  }
});
