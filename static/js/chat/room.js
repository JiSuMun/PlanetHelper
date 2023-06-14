document.addEventListener('DOMContentLoaded', () => {
  const roomName = JSON.parse(document.getElementById('room-name').textContent);
  const username = document.getElementById('username').value;

  let loc = window.location;
  let wsStart = 'ws://';
  if (loc.protocol == 'https:') {
    wsStart = 'wss://';
  }

  const chatSocket = new WebSocket(
    wsStart + window.location.host + '/ws/chat/' + roomName + '/'
  );

  chatSocket.onopen = function (event) {
    console.log('WebSocket connection established.');
  };

  chatSocket.onmessage = function (event) {
    const message = JSON.parse(event.data);
    console.log('Received message:', message);
    displayMessage({
      sender: message.sender,
      content: message.message,
      formatted_timestamp: message.formatted_timestamp,
    });
  };


  chatSocket.onclose = function (event) {
    console.log('WebSocket connection closed.');
  };

  chatSocket.onerror = function (event) {
    console.error('WebSocket error:', event);
  };

  const form = document.getElementById('text_form');
  const messageInput = document.getElementById('message_input');

  form.addEventListener('submit', function (event) {
    event.preventDefault();
    const message = messageInput.value.trim();
    if (message !== '') {
      const messageData = {
        'message': message
      };
      chatSocket.send(JSON.stringify(messageData));
      messageInput.value = '';
    }
  });

  function displayMessage(message) {
    const chatRoom = document.getElementById('chat-room');

    const noMessagesElement = chatRoom.querySelector('p');
    if (noMessagesElement && noMessagesElement.textContent === "No messages yet.") {
      chatRoom.removeChild(noMessagesElement);
    }

    const messageElement = document.createElement('div');
    messageElement.classList.add('message');

    if (message.sender === username) {
      messageElement.classList.add('my-message');
    } else {
      messageElement.classList.add('other-message');

      const username = document.createElement('p');
      username.textContent = message.sender;
      messageElement.appendChild(username);
    }

    const content = document.createElement('p');
    content.textContent = message.content;
    messageElement.appendChild(content);

    const timestamp = document.createElement('p');
    timestamp.textContent = message.formatted_timestamp;
    messageElement.appendChild(timestamp);

    chatRoom.appendChild(messageElement);
    chatRoom.scrollTop = chatRoom.scrollHeight;
    scrollToBottom();
  }

  function scrollToBottom() {
    const chatRoom = document.getElementById('chat-room');
    chatRoom.scrollTop = chatRoom.scrollHeight;
    }
    
    scrollToBottom();
});
