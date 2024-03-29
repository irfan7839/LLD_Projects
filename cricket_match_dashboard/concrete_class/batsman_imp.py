from LLD_Projects.cricket_match_dashboard.interfaces.batsman import Batsman


class BatsmanImp(Batsman):
    def __init__(self):
        self.player = None
        self.runs = 0
        self.balls = 0
        self.fours = 0
        self.sixes = 0
        self.strike_rate = 0
        self.is_out = False

    def create_batsman(self, player):
        self.player = player

    def update_runs(self, score):
        if score == '4':
            self.fours += 1
            self.balls += 1
            self.runs += 4
            self.strike_rate = self.runs / self.balls
        elif score == '6':
            self.sixes += 1
            self.balls += 1
            self.runs += 6
            self.strike_rate = self.runs / self.balls
        elif score in ['0', '1', '2', '3']:
            self.runs += int(score)
            self.balls += 1
            self.strike_rate = self.runs / self.balls
        elif score == 'out':
            self.is_out = True
