# Real-Time Dice Game Web Application

## Overview

This project is a real-time dice game web application built using Python's Flask and Flask-SocketIO libraries. It allows users to create and join game rooms, play a dice-based game against a bot with varying difficulty levels, and track game results. The user interface is designed with HTML, CSS, and JavaScript for a modern and intuitive experience.

## Features

- **Create and Join Rooms:** 
  - Users can create unique game rooms with a generated UUID.
  - Join existing rooms with a unique room ID.
  - The server manages the game state for each room to ensure a seamless multiplayer experience.

- **Start Game:** 
  - Customize game settings, including bot difficulty, initial money, and the number of rounds.
  - Start the game once players are ready in the room.

- **Dice Rolling Mechanics:**
  - Players roll dice against a bot, with the bot’s difficulty impacting its dice results.
  - Bot difficulty levels range from easy to ultimate, each with different strategies for dice outcomes.

- **Real-Time Updates:** 
  - Utilizes Flask-SocketIO for real-time communication.
  - Provides live updates for actions such as starting the game, rolling dice, and displaying results.

- **Game Results:**
  - Displays the outcome of each round, including the results of each player's rolls, the bot’s rolls, and the impact on the money based on game settings.

## Key Components

- **Backend (Flask & Flask-SocketIO):** 
  - Manages game rooms, player actions, and game state.
  - Handles real-time communication and game logic.

- **Frontend (HTML, CSS, and JavaScript):** 
  - Provides a user-friendly interface for interacting with the game.
  - Includes features for creating rooms, joining rooms, and viewing game results.

- **Dice Game Logic (`dice_game.py`):** 
  - Defines the dice game mechanics.
  - Includes different bot strategies and dice roll outcomes.

## Usage

- **Create a Room:** 
  - Click the "Create Room" button to generate a new game room and receive a unique room ID.

- **Join a Room:** 
  - Enter the room ID to join an existing game room.

- **Start the Game:** 
  - Once players are in the room, set the game parameters (bot difficulty, money, rounds) and start the game.

- **Roll Dice:** 
  - Players and the bot roll dice, with results displayed in real-time.

- **View Results:** 
  - After the game ends, view the results to see who won and how the money changed.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
