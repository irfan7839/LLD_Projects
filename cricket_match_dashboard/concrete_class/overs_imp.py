from interfaces.overs import Overs


class OversImp(Overs):

    def __init__(self):
        self.over = []
        self.total_runs = 0
        self.total_wicket = 0
        self.total_extras = 0
        self.score_list = ['0', '1', '2', '3', '4', '6']
        self.extra = ['wd', 'nb']
        self.ball_count = 0
        self.score = 0
        self.current_bowler = None
        self.previous_bowler = None

    def add_ball_update(self, score):

        self.over.append(score)
        self.score = score
        if score in self.extra:
            self.total_extras += 1
        elif score != 'out':
            self.total_runs += int(score)
            self.ball_count += 1
        elif score == 'out':
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

    def start_over(self, batting_team, bowling_team, inning, bt1=None):
        over = OversImp()
        score_list = ['1', '2', '3', '4', '6', 'wd', 'nb', 'out', '0']
        print('score can be selected')
        while over.ball_count < 6:
            print(score_list)
            score = input('please select from above options')
            if score not in score_list:
                print('please select correct value')
            else:

                over.add_ball_update(score)
                batting_team.update_team_scores(score)
                batting_team.update_current_batsman_stat(score)
                bowling_team.update_current_bowlers_state(score)
                inning_over = batting_team.get_new_batsman(score)
                if inning_over:
                    return True
                batting_team.change_batsman(score)
                batting_team.show_current_batting_team_stats()
                bowling_team.show_current_bowling_team_stats()
            if inning == 2:
                if self.total_run > bt1.total_run:
                    return True
                self.show_runs_required_to_win()
        if over.ball_count == 6:
            print('Over finished please change the bowler')
            self.previous_bowler = self.current_bowler
            self.current_bowler = None
        return False