const chatBox = document.getElementById("chat-box");
const userInput = document.getElementById("user-input");
// asynchronous function to send user input and receive response
document.getElementById("user-input").addEventListener("keypress", function(e) {
  if (e.key === "Enter") sendMessage();
});

async function sendMessage() {
  const message = userInput.value.trim();
  if (!message) return;
//means if input nahi hai toh return kardo
  appendMessage(message, "user");
  userInput.value = "";

 // const response = await fetch("http://localhost:5000/chat", {
  const response = await fetch("https://aura-backend-qkyj.onrender.com/invoke", {
//isme not sure but url invoke hai
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ message })
  });
//
  const data = await response.json();
  appendMessage(data.response, "bot");
}
//append function to display messages in the chat box
function appendMessage(msg, type) {
  const messageDiv = document.createElement("div");
  messageDiv.classList.add("message", type);
  messageDiv.textContent = msg;
  chatBox.appendChild(messageDiv);
  chatBox.scrollTop = chatBox.scrollHeight;
}
//document.getElementById("send-button").addEventListener("click", sendMessage);
//userInput.addEventListener("keypress", function(event) {
  //if (event.key === "Enter") {
  //  event.preventDefault();
   // sendMessage();
  //}
//});
