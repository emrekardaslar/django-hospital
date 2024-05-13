// myapp/static/js/mywebsocket.js

const socket = new WebSocket("ws://" + window.location.host + "/ws/hospital/");
socket.onopen = function (event) {
  console.log("WebSocket is connected.");
};

socket.onmessage = function (event) {
  const messageContainer = document.getElementById("message-container");
  const message = JSON.parse(event.data).message;
  messageContainer.innerHTML += `<p>${message}</p>`;
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

document.addEventListener("DOMContentLoaded", function () {
  const sendButton = document.querySelector("button");

  // Event listener for Send button click
  sendButton.addEventListener("click", sendMessage);

  // Event listener for pressing Enter key
  document.addEventListener("keypress", function (event) {
    if (event.key === "Enter") {
      sendMessage();
    }
  });

  // Focus on the input field when the page loads
  document.getElementById("message-input").focus();
});
