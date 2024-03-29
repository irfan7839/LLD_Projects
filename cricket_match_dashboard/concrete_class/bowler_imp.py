from abc import abstractmethod

from interfaces.bowler import Bowler


class BowlerImp(Bowler):

    def __init__(self):
        self.player = None
        self.over = 0
        self.total_balls = 0
        self.runs = 0
        self.maiden = 0
        self.wicket = 0
        self.economy = 0
        self.dot_balls = 0
        self.six_conceded = 0
        self.four_conceded = 0
        self.is_over_finished = False
        self.is_last_bowler = False

    # def get_bowler(self, player_id):
    #     for player in self.
    def create_bowler(self, player):
        self.player = player

    def update_state(self, score):
        if score == '0':
            self.dot_balls += 1
            self.total_balls += 1
            self.economy = self.runs / self.total_balls
        elif score == 'out':
            self.wicket += 1
            self.total_balls += 1
            self.economy = self.runs / self.total_balls
        elif score == '4':
            self.runs += int(score)
            self.four_conceded += 1
            self.total_balls += 1
            self.economy = self.runs / self.total_balls
        elif score == '6':
            self.runs += int(score)
            self.six_conceded += 1
            self.total_balls += 1
            self.economy = self.runs / self.total_balls
        elif score == 'wd' or score == 'nb':
            self.runs += 1
            self.economy = self.runs / self.total_balls
        elif score == '1' or score == '2' or score == '3':
            self.runs += int(score)
            self.total_balls += 1
            self.economy = self.runs / self.total_balls
        if self.total_balls != 0 and self.total_balls % 6 == 0:
            self.over += 1
            self.is_over_finished = True
        else:
            self.is_over_finished = False

    def change_bowler(self):
        if self.is_over_finished:
            print("over finished please change bowler")
