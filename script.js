// Establish socket connection
var socket = io();

// Function to start the game
function startGame() {
    // Get form values
    var botOption = parseInt(document.getElementById('botOption').value);
    var rounds = parseInt(document.getElementById('rounds').value);
    var money = parseInt(document.getElementById('money').value);

    // Ensure values are valid
    if (isNaN(botOption) || isNaN(rounds) || isNaN(money)) {
        alert("Please fill out all fields correctly.");
        return;
    }

    // Emit the start_game event with the form data
    socket.emit('start_game', {
        room: 'default_room', // Replace with actual room logic if needed
        bot_option: botOption,
        money: money,
        rounds: rounds
    });
}

// Listen for the 'game_started' event
socket.on('game_started', function(data) {
    document.getElementById('result').innerText = 'Game started with bot option: ' + data.bot_option;
    // Additional logic to update the UI as needed
});

// Handle any errors
socket.on('error', function(data) {
    alert(data.message);
});
