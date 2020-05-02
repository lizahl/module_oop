from exceptions import EnemyDown, Score, GameOver
from models import Enemy, Player
from datetime import datetime
from time import strftime
from termcolor import colored

def start(chosen_fighter):

    go = input('Type "START" to start \t')
    level = 1
    Round = 1
    fighter2 = Enemy(level)
    while True:
        print(colored("\n\n+------------------------------------------------------+\n"
              "\t\t\t\tLEVEL:\t{}\tROUND:\t{} \n\t\t\t\t\t\tFIGHT".format(level, Round), 'red'))
        print(colored("+------------------------------------------------------+\n", 'red'))
        try:
            result = chosen_fighter.attack(fighter2)
        except EnemyDown:
            print("\t\t\t\tYOUR ENEMY IS DEAD!")
            level += 1
            Player.expscore += 5
            Round = 1
            fighter2 = Enemy(level)
            print(colored("\t\t\tYOU ARE SCORED {} POINTS.".format(Player.print_scores()), 'red'))
        else:
            print(colored("\t\t\t\tYOUR LIVES:\t{} | ENEMY LIVES:{}".
                          format(chosen_fighter.lives, fighter2.lives), 'blue'))
            result = chosen_fighter.defence(fighter2)
            if result == 0 or result == -1:
                print("\t\t\t\t\tNEW ROUND!")
                Round += 1
            elif result == 1:
                print("\t\t\t\t\t\t-1 LIFE")
                chosen_fighter.decrease_lives()
                print(colored("\t\t\t\tYOUR LIVES:\t{} | ENEMY LIVES:{}".
                              format(chosen_fighter.lives,fighter2.lives),'blue'))
                Round += 1


if __name__ == '__main__':
    name = input("Enter your name:\t")
    print('Hi, {}'.format(name),'!')
    gamer = Player(name)
    try:
        start(gamer)
    except GameOver:
        print(colored("\t\t\t\tYOU ARE SCORED {} POINTS.".format(Player.print_scores()), 'red'))
        dt = datetime.now()
        dt = strftime('%Y-%m-%d %H:%M:%S', datetime.timetuple(dt))
        current = Score(dt, gamer.name, gamer.expscore)
        records = Score.records('scores.txt')
        records.append(current)
        records.sort(key=lambda record: record.score, reverse=True)
        for item in range(0, 10):
            records[item].write_result()
    except KeyboardInterrupt:
        pass
    finally:
        Player.expscore = 0
        print("\t\t\t\t\t\tGOODBYE!")
