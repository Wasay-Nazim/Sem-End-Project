console.log('Script Loaded!');

let micBtn = document.getElementById('mic-btn');
let chatbox = document.getElementById('chatbox');

let SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
let recognition = new SpeechRecognition();

recognition.lang = 'en-US';
recognition.interimResults = false;

function appendMessage(content, type) {
    const msgDiv = document.createElement('div');
    msgDiv.classList.add('message', type);
    msgDiv.textContent = content;
    chatbox.appendChild(msgDiv);
    chatbox.scrollTop = chatbox.scrollHeight;
}

function processCommand(command) {
    appendMessage(command, 'user');

    let response = '';
    try {
        if (command.includes('what is this website about')) {
            response = 'This website is an e-commerce platform for shoes.';
        } else if (command.includes('who are you')) {
            response = 'I am Haaru, your personal assistant, created to assist you with your queries.';
        } else if (command.includes('what time is it')) {
            response = `The current time is ${new Date().toLocaleTimeString()}.`;
        } else if (command.includes('what is the date today')) {
            response = `Today is ${new Date().toLocaleDateString()}.`;
        } else if (command.includes('show me the sale')) {
            response = 'Sure! Redirecting you to the sale page.';
            window.open('/a');
        } else if (command.includes('show me something under')) {
            let amount = command.match(/\d+/);
            if (amount) {
                if (amount < 1000) {
                    response = `Sure! Redirecting you to items under ${amount} Rs.`;
                    window.open('/c');
                } else if (amount < 5000 || amount < 6000) {
                    response = `Sure! Redirecting you to items under ${amount} Rs.`;
                    window.open('/b');
                } else if (amount < 7000) {
                    response = `Sure! Redirecting you to items under ${amount} Rs.`;
                    window.open('/aa');
                } else {
                    response = `Sure! Redirecting you to items over ${amount} Rs.`;
                    window.open('/d');
                }
            } else {
                response = 'Could you please specify the amount?';
            }
        } else if (command.includes('premium collection')) {
            response = 'Here is our premium collection.';
            window.open('/premium');
        } else if (command.includes('thank you')) {
            response = 'You are welcome! Feel free to ask me anything.';
        } else if (command.includes('hello') || command.includes('hi')) {
            response = 'Hello! How can I assist you today?';
        } else if (command.includes('goodbye') || command.includes('bye')) {
            response = 'Goodbye! Have a great day!';
        } else if (command.includes('how are you')) {
            response = 'I am just a program, but thank you for asking! How can I help you today?';
        } else if (command.includes('what is your name')) {
            response = 'My name is Haaru, your assistant.';
        } else if (command.includes('what can you do')) {
            response = 'I can assist you with product queries, navigate the website, and answer general questions. What would you like to do?';
        } else if (command.includes('go to login')) {
            response = 'Redirecting you to the login page.';
            window.open('/login');
        } else if (command.includes('go to register')) {
            response = 'Redirecting you to the registration page.';
            window.open('/register');
        } else if (command.includes('go to welcome')) {
            response = 'Redirecting you to the welcome page.';
            window.open('/welcome');
        } else if (command.includes('go to home')) {
            response = 'Redirecting you to the home page.';
            window.open('/home');
        } else if (command.includes('go to products')) {
            response = 'Redirecting you to the products page.';
            window.open('/products');
        } else if (command.includes('go to men')) {
            response = 'Redirecting you to the men\'s section.';
            window.open('/men');
        } else if (command.includes('go to women')) {
            response = 'Redirecting you to the women\'s section.';
            window.open('/women');
        } else if (command.includes('go to children page')) {
            response = 'Redirecting you to the children\'s section.';
            window.open('/children');
        } else if (command.includes('go to premium')) {
            response = 'Redirecting you to the premium collection.';
            window.open('/premium');
        } else if (command.includes('go to about us')) {
            response = 'Redirecting you to the about us page.';
            window.open('/aboutus');
        } else {
            response = "I'm sorry, I didn't understand that. Could you please rephrase?";
        }

        appendMessage(response, 'assistant');
        speak(response);
    } catch (error) {
        console.error('Error processing command:', error);
        let errorMessage = 'Oops! Something went wrong while processing your command. Please try again.';
        appendMessage(errorMessage, 'assistant');
        speak(errorMessage);
    }
}

function speak(text) {
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = 'en-US';
    utterance.rate = 1;
    window.speechSynthesis.speak(utterance);
}

recognition.onresult = (event) => {
    const transcript = event.results[0][0].transcript.toLowerCase();
    processCommand(transcript);
};

recognition.onerror = (event) => {
    console.error('Speech Recognition Error:', event.error);
    let errorMessage = 'Sorry, I could not hear you properly. Please try again.';
    appendMessage(errorMessage, 'assistant');
    speak(errorMessage);
};

micBtn.addEventListener('click', () => {
    try {
        recognition.start();
        appendMessage('Listening...', 'assistant');
    } catch (error) {
        console.error('Error starting recognition:', error);
        let errorMessage = 'Failed to start voice recognition. Please check your microphone settings.';
        appendMessage(errorMessage, 'assistant');
        speak(errorMessage);
    }
});
