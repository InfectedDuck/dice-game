from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit, join_room
import dice_game as dg
import uuid

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

games = {}  # Store game state for each room

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('create_room')
def create_room(data):
    print("create_room called with data:", data)
    room_id = str(uuid.uuid4())
    games[room_id] = {'players': [], 'bot_option': None, 'money': 0, 'rounds': 0}
    emit('room_created', {'room': room_id})

@socketio.on('join_room')
def on_join(data):
    room = data['room']
    join_room(room)
    if room not in games:
        games[room] = {'players': [], 'bot_option': None, 'money': 0, 'rounds': 0}
    if request.sid not in games[room]['players']:
        games[room]['players'].append(request.sid)
    emit('player_joined', {'player': request.sid}, room=room)

@app.route('/game/<room_id>')
def game_page(room_id):
    return render_template('game.html', room_id=room_id)

@socketio.on('start_game')
def start_game(data):
    room = data.get('room')
    bot_option = data.get('bot_option')
    money = data.get('money')
    rounds = data.get('rounds')

    if not room or not bot_option or money is None or rounds is None:
        emit('error', {'message': 'Missing data.'})
        return

    if room not in games:
        games[room] = {'players': [], 'bot_option': None, 'money': 0, 'rounds': 0}

    games[room]['bot_option'] = bot_option
    games[room]['money'] = money
    games[room]['rounds'] = rounds

    emit('game_started', {'bot_option': bot_option, 'money': money, 'rounds': rounds, 'room': room})

@socketio.on('roll_dice')
def roll_dice(data):
    room = data['room']
    player_id = request.sid
    bot_option = games[room]['bot_option']
    money = games[room]['money']
    rounds = games[room]['rounds']

    if player_id not in games[room]['players']:
        return

    user = dg.User()
    bot = get_bot_instance(bot_option)
    bot_result1 = bot_result2 = user_result1 = user_result2 = 0
    results = []

    for _ in range(rounds):
        if bot_option == 1:
            bot_result1_dice, bot_result2_dice = bot.bot_roll_easy()
        elif bot_option == 2:
            bot_result1_dice, bot_result2_dice = bot.bot_roll_medium()
        elif bot_option == 3:
            bot_result1_dice, bot_result2_dice = bot.bot_roll_hard()
        elif bot_option == 4:
            bot_result1_dice, bot_result2_dice = bot.bot_roll_ultimate()

        user_result1_dice, user_result2_dice = user.roll_dice()
        bot_result1 += dg.dictionary_of_dices[bot_result1_dice]
        bot_result2 += dg.dictionary_of_dices[bot_result2_dice]
        user_result1 += dg.dictionary_of_dices[user_result1_dice]
        user_result2 += dg.dictionary_of_dices[user_result2_dice]

        results.append({
            'user_rolls': (user_result1_dice, user_result2_dice),
            'bot_rolls': (bot_result1_dice, bot_result2_dice)
        })

    bot_total = bot_result1 + bot_result2
    user_total = user_result1 + user_result2

    if bot_total > user_total:
        money_return = 0
        result = "Bot has won! You lost: " + str(money_return)
    elif bot_total < user_total:
        money_return = dg.amount_of_money(bot_option, money)
        result = "You have won! You gain: " + str(money_return)
    else:
        result = "Draw!"
    
    emit('game_result', {
        'result': result,
        'user_results': results,
        'bot_total': bot_total,
        'user_total': user_total,
        'money': money
    }, room=room)

def get_bot_instance(bot_option):
    if bot_option == 1:
        return dg.EasyBot()
    elif bot_option == 2:
        return dg.MediumBot()
    elif bot_option == 3:
        return dg.HardBot()
    elif bot_option == 4:
        return dg.UltimateBot()

if __name__ == '__main__':
    socketio.run(app, debug=True)
