import random as r

dictionary_of_dices = {'⚀': 1, '⚁': 2, '⚂': 3, '⚃': 4, '⚄': 5, '⚅': 6}

class EasyBot:
    def __init__(self):
        self.outcomes = [
            ('⚀', '⚀', 5), ('⚀', '⚁', 4), ('⚀', '⚂', 10), ('⚀', '⚃', 10),
            ('⚀', '⚄', 10), ('⚀', '⚅', 10), ('⚁', '⚀', 10), ('⚁', '⚁', 10),
            ('⚁', '⚂', 5), ('⚁', '⚃', 5), ('⚁', '⚄', 10), ('⚁', '⚅', 10)
        ]

    def roll_dice(self):
        return r.randint(1, 6), r.randint(1, 6)

    def bot_roll_easy(self):
        rand_num = r.randint(1, 100)
        cumulative_chance = 0
        for outcome in self.outcomes:
            cumulative_chance += outcome[2]
            if rand_num <= cumulative_chance:
                return outcome[0], outcome[1]
        return self.roll_dice()

class MediumBot:
    def __init__(self):
        self.outcomes = [
            ('⚀', '⚅', 5), ('⚁', '⚀', 5), ('⚁', '⚁', 5), ('⚁', '⚂', 5),
            ('⚁', '⚃', 10), ('⚁', '⚄', 10), ('⚁', '⚅', 10), ('⚂', '⚀', 10),
            ('⚂', '⚁', 10), ('⚂', '⚂', 10), ('⚂', '⚃', 5), ('⚂', '⚄', 5),
            ('⚂', '⚅', 5), ('⚃', '⚀', 3), ('⚃', '⚁', 2)
        ]

    def roll_dice(self):
        return r.randint(1, 6), r.randint(1, 6)

    def bot_roll_medium(self):
        rand_num = r.randint(1, 100)
        cumulative_chance = 0
        for outcome in self.outcomes:
            cumulative_chance += outcome[2]
            if rand_num <= cumulative_chance:
                return outcome[0], outcome[1]
        return self.roll_dice()

class HardBot:
    def __init__(self):
        self.outcomes = [
            ('⚀', '⚅', 2), ('⚁', '⚄', 3), ('⚂', '⚃', 4), ('⚃', '⚅', 5),
            ('⚄', '⚅', 6)
        ]

    def roll_dice(self):
        return r.randint(1, 6), r.randint(1, 6)

    def bot_roll_hard(self):
        rand_num = r.randint(1, 100)
        cumulative_chance = 0
        for outcome in self.outcomes:
            cumulative_chance += outcome[2]
            if rand_num <= cumulative_chance:
                return outcome[0], outcome[1]
        return self.roll_dice()

class UltimateBot:
    def __init__(self):
        self.outcomes = [
            ('⚀', '⚀', 1), ('⚁', '⚁', 2), ('⚂', '⚂', 3), ('⚃', '⚃', 4),
            ('⚄', '⚄', 5), ('⚅', '⚅', 6)
        ]

    def roll_dice(self):
        return r.randint(1, 6), r.randint(1, 6)

    def bot_roll_ultimate(self):
        rand_num = r.randint(1, 100)
        cumulative_chance = 0
        for outcome in self.outcomes:
            cumulative_chance += outcome[2]
            if rand_num <= cumulative_chance:
                return outcome[0], outcome[1]
        return self.roll_dice()

class User:
    def __init__(self):
        self.outcomes = [
            ('⚀', '⚀'), ('⚀', '⚁'), ('⚀', '⚂'), ('⚀', '⚃'),
            ('⚀', '⚄'), ('⚀', '⚅'), ('⚁', '⚀'), ('⚁', '⚁'),
            ('⚁', '⚂'), ('⚁', '⚃'), ('⚁', '⚄'), ('⚁', '⚅'),
            ('⚂', '⚀'), ('⚂', '⚁'), ('⚂', '⚂'), ('⚂', '⚃'),
            ('⚂', '⚄'), ('⚂', '⚅'), ('⚃', '⚀'), ('⚃', '⚁'),
            ('⚃', '⚂'), ('⚃', '⚃'), ('⚃', '⚄'), ('⚃', '⚅'),
            ('⚄', '⚀'), ('⚄', '⚁'), ('⚄', '⚂'), ('⚄', '⚃'),
            ('⚄', '⚄'), ('⚄', '⚅'), ('⚅', '⚀'), ('⚅', '⚁'),
            ('⚅', '⚂'), ('⚅', '⚃'), ('⚅', '⚄'), ('⚅', '⚅')
        ]

    def roll_dice(self):
        return r.choice(['⚀', '⚁', '⚂', '⚃', '⚄', '⚅']), r.choice(['⚀', '⚁', '⚂', '⚃', '⚄', '⚅'])

def amount_of_money(option, money):
    dictionary_of_money = {1: 1.5, 2: 3.0, 3: 5.0, 4: 10.0}
    coefficient = dictionary_of_money[option]
    money_after = round(money * coefficient)
    return money_after
