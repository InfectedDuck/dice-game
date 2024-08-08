document.addEventListener('DOMContentLoaded', () => {
    const socket = io();
    const room = window.location.pathname.split('/').pop();
    const rollButton = document.getElementById('roll');
    const increaseMoneyButton = document.getElementById('increaseMoney');
    const infoDiv = document.getElementById('info');
    const winnerDiv = document.getElementById('winner');
    const userRollsDiv = document.getElementById('userRolls');
    const botRollsDiv = document.getElementById('botRolls');

    socket.emit('join_room', { room: room });

    socket.on('game_update', (data) => {
        infoDiv.textContent = `Money: ${data.money}, Rounds Left: ${data.rounds}`;
        if (data.winner) {
            winnerDiv.textContent = `Winner: ${data.winner}`;
        } else {
            winnerDiv.textContent = '';  // Clear winner information if no winner
        }
    });

    rollButton.addEventListener('click', () => {
        socket.emit('roll_dice', { room: room });
    });

    increaseMoneyButton.addEventListener('click', () => {
        socket.emit('increase_money', { room: room });
    });

    socket.on('game_result', (data) => {
        // Show the results of the dice rolls
        let userRolls = data.user_results.map((result, index) => 
            `Round ${index + 1}: User rolled ${result.user_rolls.join(', ')}`
        ).join('<br>');

        let botRolls = data.user_results.map((result, index) => 
            `Round ${index + 1}: Bot rolled ${result.bot_rolls.join(', ')}`
        ).join('<br>');

        userRollsDiv.innerHTML = `<strong>Your Rolls:</strong><br>${userRolls}`;
        botRollsDiv.innerHTML = `<strong>Bot Rolls:</strong><br>${botRolls}`;
        
        // Show the result and money update
        winnerDiv.textContent = `Result: ${data.result}`;
        infoDiv.textContent = `Money: ${data.money} | User Total: ${data.user_total} | Bot Total: ${data.bot_total}`;
    });

    socket.on('error', (data) => {
        alert(data.message);
    });
});
