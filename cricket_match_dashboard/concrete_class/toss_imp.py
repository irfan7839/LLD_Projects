from interfaces.toss import Toss
import random


class TossImp(Toss):

    def __init__(self):
        self.coin = ['Heads', 'Tail']
        self.result = None

    def toss_time(self):
        value = input("team1 please select Heads or tail")
        coin_value = random.choice(self.coin)
        if coin_value == value:
            self.result = 'Team1'
            print('team1 won the toss')
        else:
            print('team1 loss the toss')
            self.result = 'Team2'

    def toss_result(self):
        return self.result
