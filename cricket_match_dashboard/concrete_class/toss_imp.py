
import random

from interfaces.toss import Toss


class TossImp(Toss):

    def __init__(self):
        self.coin = ['1', '2']
        self.result = None

    def toss_time(self, team_name):
        while True:
            value = input(f"{team_name} please select 1 for heads or 2 for tails")
            if value not in self.coin:
                print("please choose a valid value")
            else:
                break
        coin_value = random.choice(self.coin)
        if coin_value == value:
            self.result = 'won'
            print(f'{team_name} won the toss')
        else:
            print(f'{team_name} loss the toss')
            self.result = 'loss'

    def toss_result(self):
        return self.result
