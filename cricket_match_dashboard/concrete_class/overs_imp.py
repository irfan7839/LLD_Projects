from LLD_Projects.cricket_match_dashboard.interfaces.overs import Overs


class OversImp(Overs):

    def __init__(self):
        self.over = []
        self.total_runs = 0
        self.total_wicket = 0
        self.total_extras = 0
        self.extras = ['wd', 'nb']
        self.out = ['bowled', 'caught', 'lbw']
        self.ball_count = 0
        self.score = 0

    def add_ball_update(self, score):
        self.over.append(score)
        self.score = score
        if score in self.extras:
            self.total_extras += 1
        elif score not in self.out:
            self.total_runs += int(score)
            self.ball_count += 1
        elif score in self.out:
            self.total_wicket += 1
            self.ball_count += 1

    def show_no_of_balls(self):
        if self.ball_count < 6:
            print(f"{self.score} scored on {self.ball_count}th ball")
        if self.ball_count == 6:
            print(f"{self.score} scored on {self.ball_count}th ball")
            print("Over Completed")

    def total_score_in_over(self):
        return self.total_runs
