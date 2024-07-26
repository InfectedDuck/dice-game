import random as r
import time
def welcoming():
    print("Hello, this is a new dice game, make an option, choose between easy medium hard bot and ULTIMATE Bot! Try your luck!")
    print("Currently you have: ", 5000,"Tenge")
    print("1.Easy BOT, you dont need a good luck to win, coefficient=1.5")
    print("2.Medium BOT, you shall prepare in using your luck! Coefficient=3.0")
    print("3.Hard BOT, if you win him you are a lucky man, go and buy lottery tickets! Coefficient=5.0")
    print("4.ULTIMATE BOT, there is a very small chance to win! Coefficient=10.0!")
    bot_option=int(input("Write an option in there"))
    rounds=int(input("Write how many rounds you want to play"))
    money=int(input("Insert the amount of money you want to use"))
    return bot_option,rounds,money
dictionary_of_dices={'⚀':1, '⚁':2, '⚂':3,'⚃':4,'⚄':5,'⚅':6}
bot_result1=0
bot_result2=0
user_result1=0
user_result2=0
class EasyBot:
    def __init__(self):
        self.easy_outcomes = [
            ('⚀', '⚀', 5),
            ('⚀', '⚁', 4),
            ('⚀', '⚂', 10),
            ('⚀', '⚃', 10),
            ('⚀', '⚄', 10),
            ('⚀', '⚅', 10),
            ('⚁', '⚀', 10),
            ('⚁', '⚁', 10),
            ('⚁', '⚂', 5),
            ('⚁', '⚃', 5),
            ('⚁', '⚄', 10),
            ('⚁', '⚅', 10),
        ]
        self.medium_outcomes = [
            ('⚀', '⚅', 5),
            ('⚁', '⚀', 5),
            ('⚁', '⚁', 5),
            ('⚁', '⚂', 5),
            ('⚁', '⚃', 10),
            ('⚁', '⚄', 10),
            ('⚁', '⚅', 10),
            ('⚂', '⚀', 10),
            ('⚂', '⚁', 10),
            ('⚂', '⚂', 10),
            ('⚂', '⚃', 5),
            ('⚂', '⚄', 5),
            ('⚂', '⚅', 5),
            ('⚃', '⚀', 3),
            ('⚃', '⚁', 2),
        ]
        self.hard_outcomes =[
            ()
        ]
    def roll_dice(self):
        return r.randint(1, 6), r.randint(1, 6)
    def bot_roll_easy(self,bot_option):
        outcomes=
        rand_num = r.randint(1, 100)
        cumulative_chance = 0
        for outcome in self.outcomes:
            cumulative_chance += outcome[2]
            if rand_num <= cumulative_chance:
                return outcome[0], outcome[1]
        return self.roll_dice()
bot_option,rounds,money=welcoming()
class User:
    def __init__(self):
        self.outcomes=[
            ('⚀', '⚀'),
            ('⚀', '⚁'),
            ('⚀', '⚂'),
            ('⚀', '⚃'),
            ('⚀', '⚄'),
            ('⚀', '⚅'),
            ('⚁', '⚀'),
            ('⚁', '⚁'),
            ('⚁', '⚂'),
            ('⚁', '⚃'),
            ('⚁', '⚄'),
            ('⚁', '⚅'),
            ('⚂', '⚀'),
            ('⚂', '⚁'),
            ('⚂', '⚂'),
            ('⚂', '⚃'),
            ('⚂', '⚄'),
            ('⚂', '⚅'),
            ('⚃', '⚀'),
            ('⚃', '⚁'),
            ('⚃', '⚂'),
            ('⚃', '⚃'),
            ('⚃', '⚄'),
            ('⚃', '⚅'),
            ('⚄', '⚀'),
            ('⚄', '⚁'),
            ('⚄', '⚂'),
            ('⚄', '⚃'),
            ('⚄', '⚄'),
            ('⚄', '⚅'),
            ('⚅', '⚀'),
            ('⚅', '⚁'),
            ('⚅', '⚂'),
            ('⚅', '⚃'),
            ('⚅', '⚄'),
            ('⚅', '⚅')
        ]
    def roll_dice(self):
        return r.choice(['⚀', '⚁', '⚂', '⚃', '⚄', '⚅']), r.choice(['⚀', '⚁', '⚂', '⚃', '⚄', '⚅'])
def amount_of_money(self,option,money):
    dictionary_of_money={1:1.5,2:3.0,3:5,4:10}
    coefficient=dictionary_of_money[option]
    money_after=round(money*coefficient)
    return money_after

if bot_option==1:
    for i in range(rounds):
        bot_result1_dice,bot_result2_dice=EasyBot().bot_roll_easy()
        user_result1_dice,user_result2_dice=User().roll_dice()
        bot_result1+=dictionary_of_dices[bot_result1_dice]
        bot_result2+=dictionary_of_dices[bot_result2_dice]
        user_result1+=dictionary_of_dices[user_result1_dice]
        user_result2+=dictionary_of_dices[bot_result2_dice]
        print("Bot's round: ", bot_result1_dice,bot_result2_dice)
        print("User's round: ", user_result1_dice,user_result2_dice)
    if bot_result1+bot_result2>user_result1+user_result2:
        money_return=0
        print("Bot has won! You lost: ", money_return, "Want to try again?")
    elif bot_result1+bot_result2<user_result1+user_result2:
        money_return=amount_of_money(bot_option,money)
        print("You have win! You gain: ", money_return, "\nYou are on fire! Try your luck again!")
    else:
        print("Draw! Wann try again?")



