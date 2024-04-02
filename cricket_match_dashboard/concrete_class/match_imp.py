from concrete_class.batsman_imp import BatsmanImp
from concrete_class.bowler_imp import BowlerImp
from concrete_class.player_imp import PlayerImp
from concrete_class.team_imp import TeamImp
from concrete_class.overs_imp import OversImp
from concrete_class.toss_imp import TossImp
from interfaces.match import Matches
from LLD_Projects.cricket_match_dashboard.concrete_class.batting_team import BattingTeamImp
from LLD_Projects.cricket_match_dashboard.concrete_class.bowling_team_imp import BowlingTeamImp


class MatchImp(Matches):

    def __init__(self):
        self.total_players = 0
        self.total_overs = 0
        self.team1 = None
        self.team2 = None
        self.team1_bowlers = []
        self.team1_extras = 0
        self.team2_extras = 0
        self.team1_batsmen = []
        self.team2_batsmen = []
        self.team2_bowlers = []
        self.total_overs_1 = 0
        self.total_wicket_1 = 0
        self.total_run_1 = 0
        self.total_overs_2 = 0
        self.total_wicket_2 = 0
        self.total_run_2 = 0
        self.total_run_needed = 0
        self.toss_result = None
        self.current_batting_team = None
        self.current_bowling_team = None
        self.current_bowler = None
        self.previous_bowler = None
        self.striker = None
        self.non_striker = None
        self.total_balls_1 = 0
        self.total_balls_2 = 0
        self.team1_run_rate = 0
        self.team2_run_rate = 0
        self.inning = 0
        self.match_winner = None
        self.first_inning_total = 0
        self.batting_team1 = None
        self.batting_team2 = None

    def select_team_for_match(self):
        while True:
            total_players = input("select number of players  ")
            if total_players.isdigit() and int(total_players) > 2:
                self.total_players = int(total_players)
                break
            else:
                print("please select correct input, total players should be greater than 2")
                continue
        t1 = TeamImp()
        t1.create_team()
        for i in range(int(total_players)):
            p = PlayerImp()
            p.create_player(f'{t1.team_name}_0{i + 1}')
            t1.add_player(p)
        self.team1 = t1
        t2 = TeamImp()
        t2.create_team()
        for i in range(int(total_players)):
            q = PlayerImp()
            q.create_player(f'{t2.team_name}_0{i + 1}')
            t2.add_player(q)
        self.team2 = t2

        while True:
            overs = input('please select total overs of a inning')
            if overs.isdigit():
                self.total_overs = int(overs)
                break
            else:
                self.total_overs = overs
                print("please select correct input")
                continue

    def toss_results(self):
        while True:
            which_team_call = input(f"choose which team will call {self.team1.team_name} or {self.team2.team_name}")
            toss = TossImp()
            team_a = None
            team_b = None
            if which_team_call not in [self.team1.team_name, self.team2.team_name]:
                continue
            else:
                if which_team_call == self.team1.team_name:
                    team_a = self.team1
                    team_b = self.team2

                elif which_team_call == self.team2.team_name:
                    team_a = self.team2
                    team_b = self.team1

                toss.toss_time(which_team_call)
                self.toss_result = toss.toss_result()

                if self.toss_result == 'won':
                    decision = input(f'{team_a.team_name} won the toss please choose bat or bowl first')
                    if decision == 'bat':
                        self.team1 = team_a
                        self.team2 = team_b
                    else:
                        self.team1 = team_b
                        self.team2 = team_a
                else:
                    decision = input(f'{team_b.team_name} won the toss please choose bat or bowl first')
                    if decision == 'bat':
                        self.team1 = team_b
                        self.team2 = team_a
                    else:
                        self.team1 = team_a
                        self.team2 = team_b
                self.current_batting_team = self.team1
                self.current_bowling_team = self.team2
                return

    def show_runs_required_to_win(self):
        if self.inning == 2:
            required_run = (self.first_inning_total - self.batting_team2.total_run) + 1
            balls_left = (self.total_overs * 6) - self.batting_team2.total_balls
            wickets_left = self.total_players - self.batting_team2.total_wicket - 1
            print(f"{required_run} runs required in {balls_left} balls with {wickets_left} wickets remaining")
        else:
            return

    def match_result(self):
        if (
                self.batting_team2.total_overs == self.total_overs or self.batting_team2.total_wicket == self.total_players - 1) and self.batting_team2.total_run < self.first_inning_total:
            win_run = self.first_inning_total - self.batting_team2.total_run
            self.match_winner = self.batting_team1.team
            print(f'{self.match_winner.team_name} won by {win_run} runs.')
            return
        elif (
                self.batting_team2.total_overs == self.total_overs or self.batting_team2.total_wicket == self.total_players - 1) and self.batting_team2.total_run == self.first_inning_total:
            print(f'Match Tied')
            return
        elif (
                self.batting_team2.total_overs <= self.total_overs and self.batting_team2.total_wicket < self.total_players - 1) and self.batting_team2.total_run > self.first_inning_total:
            win_wicket = self.total_players - (self.batting_team2.total_wicket + 1)
            self.match_winner = self.batting_team2.team
            print(f'{self.match_winner.team_name} won by {win_wicket} wickets')
            return
        else:
            return

    def start_match(self):
        self.select_team_for_match()
        self.toss_results()

        if self.current_batting_team == self.team1:
            print("INN")
            self.inning = 1
            batting_team_1 = BattingTeamImp()
            batting_team_1.create_batting_team(self.team1)
            batting_team_1.start_inning_select_batsman()
            self.batting_team1 = batting_team_1
            bowling_team_1 = BowlingTeamImp()
            bowling_team_1.create_bowling_team(self.team2)
            self.current_bowler = bowling_team_1.select_bowler()
            while batting_team_1.show_total_overs() < self.total_overs and batting_team_1.show_total_wickets() < self.total_players - 1:
                inning1_finish = self.start_over(batting_team_1, bowling_team_1)
                if inning1_finish or batting_team_1.show_total_overs() == self.total_overs:
                    self.first_inning_total = batting_team_1.show_total_runs()
                    break
                self.previous_bowler = self.current_bowler
                self.current_bowler = bowling_team_1.select_bowler()
            self.current_batting_team = self.team2
            self.current_bowling_team = self.team1
            print('1st inning finished')

        if self.current_batting_team == self.team2:
            self.inning = 2
            batting_team_2 = BattingTeamImp()
            batting_team_2.create_batting_team(self.team2)
            batting_team_2.start_inning_select_batsman()
            self.batting_team2 = batting_team_2
            bowling_team_2 = BowlingTeamImp()
            bowling_team_2.create_bowling_team(self.team1)
            self.current_bowler = bowling_team_2.select_bowler()
            while (
                    batting_team_2.total_overs < self.total_overs and batting_team_2.total_wicket < self.total_players - 1 and
                    batting_team_2.total_run <= self.first_inning_total):
                inning2_finish = self.start_over(batting_team_2, bowling_team_2)
                if inning2_finish or batting_team_2.total_overs == self.total_overs:
                    break
                self.previous_bowler = self.current_bowler
                self.show_runs_required_to_win()
                self.current_bowler = bowling_team_2.select_bowler()
        self.match_result()

    def start_over(self, batting_team, bowling_team):
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
            if self.inning == 2:
                if self.batting_team2.show_total_runs() > self.first_inning_total:
                    return True
                self.show_runs_required_to_win()
        if over.ball_count == 6:
            print('Over finished please change the bowler')
            self.previous_bowler = self.current_bowler
            self.current_bowler = None
        return False
