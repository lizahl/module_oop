from exceptions import EnemyDown, GameOver
from random import randint
from termcolor import colored
import settings

class Enemy:
    def __init__(self, level):
        self.lives = level
        self.level = level

    @staticmethod
    def select_attack():
        return randint(1, 3)

    def decrease_lives(self):
        self.lives -= 1
        if self.lives == 0:
            raise EnemyDown
        else:
            pass


class Player:
    def __init__(self, name):
        self.name = name
        self.lives = settings.num_lives
    expscore = 0

    @staticmethod
    def fight(allowed_attack, defense):
        win_round = ((1, 2), (2, 3), (3, 1))
        for item in win_round:
            if item[0] == allowed_attack:
                if item[1] == defense:
                    result = 1
                elif item[0] == defense:
                    result = 0
                else:
                    result = -1
            else:
                pass
        return result

    def decrease_lives(self):
        self.lives -= 1
        if self.lives == 0:
            raise GameOver
        else:
            pass

    @classmethod
    def print_scores(cls):
        return cls.expscore

    def attack(self, enemy_gamer):
        fighter1 = input("\t\t\t\tCHOOSE YOUR FIGHTER:\n\t\t\t"
                          "1 - MAGE  2 - WARRIOR  3 - THIEF\n\t\t\t\t\t\t\t")
        fighter1 = int(fighter1)
        fighter2 = enemy_gamer.select_attack()
        print(colored("\t\t\t\t\t\t{} vs {}".format(fighter1, fighter2), 'green'))
        fight_result = self.fight(fighter1, fighter2)
        if fight_result == 0:
            print("\t\t\t\t\tIT'S A DRAW!")
        elif fight_result == 1:
            print("\t\t\tYOU ATTACKED SUCCESSFULLY!\n\t\t\t\t\t+1 EXTRA POINT")
            enemy_gamer.decrease_lives()
            Player.expscore += 1
        elif fight_result == -1:
            print("\t\t\t\t\tYOU MISSED!")
        return fight_result

    def defence(self, enemy_gamer):
        fighter1 = input("\t\t\t\tCHOOSE YOUR FIGHTER:\n\t\t\t"
                          "1 - MAGE  2 - WARRIOR  3 - THIEF\n\t\t\t\t\t\t\t")
        fighter1 = int(fighter1)
        fighter2 = enemy_gamer.select_attack()
        print(colored("\t\t\t\t\t\t{} vs {}".format(fighter1, fighter2), 'green'))
        fight_result = self.fight(fighter2, fighter1)
        if fight_result == 0:
            print("\t\t\t\t\tIT'S A DRAW!")
        elif fight_result == 1:
            print("\t\t\t\t\t\tYOU MISSED!")
        elif fight_result == -1:
            print("\t\t\t\tYOUR ENEMY MISSED!")
        return fight_result
