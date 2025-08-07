var map = L.map('map').setView([51.505, -0.09], 13);

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

// chatbot code

const messageList = document.querySelector('.message-list')
const messageForm = document.querySelector('.message-form')
const messageInput = document.querySelector('.message-input')

messageForm.addEventListener('submit', (event) => {
    event.preventDefault();

    const message = messageInput.value.trim()
    if (message === 0){
        return;
    }
    console.log(message)
    const messageItem = document.createElement('li');
    messageItem.classList.add('list-group-item')
    messageItem.innerHTML = `
                        <div>
                            <b>You</b>
                        </div>
                        <div>
                            ${message}
                        </div>`;
    
    messageList.appendChild(messageItem);
    messageInput.value = '';
});

// Send message to the backend to be processed by ChatGPT

