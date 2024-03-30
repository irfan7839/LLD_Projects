from concrete_class.batsman_imp import BatsmanImp
from concrete_class.bowler_imp import BowlerImp
from concrete_class.player_imp import PlayerImp
from concrete_class.team_imp import TeamImp
from concrete_class.overs_imp import OversImp
from concrete_class.toss_imp import TossImp
from interfaces.match import Matches


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

    def select_team_for_match(self):
        while True:
            total_players = input("select number of players  ")
            if total_players.isdigit():
                self.total_players = int(total_players)
                break
            else:
                print("please select correct input")
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

    def create_batting_order(self):
        for player in self.team1.players_list:
            batsman = BatsmanImp()
            batsman.create_batsman(player)
            self.team1_batsmen.append(batsman)
        for player in self.team2.players_list:
            batsman = BatsmanImp()
            batsman.create_batsman(player)
            self.team2_batsmen.append(batsman)
        return

    def select_bowler(self, current_bowling_team):
        while True:
            print("please select bowler's id from below bowlers name")
            print("ID\t Name")
            bowling_ids = []
            for bowler in self.current_bowling_team.players_list:
                bowling_ids.append(bowler.id)
                if self.previous_bowler and self.previous_bowler.player.id == bowler.id:
                    continue
                else:
                    print(f"{bowler.id}\t {bowler.name}")
            bowler_id = input(f'please select bowlers id ')
            if bowler_id not in bowling_ids:
                print("please select correct bowler")
                continue
            if self.previous_bowler and bowler_id == self.previous_bowler.player.id:
                print("one bowler can't bowl two consecutive overs")
                continue
            else:
                bowler = BowlerImp()
                bowl_player = self.current_bowling_team.get_player(bowler_id)
                existing = False
                for bow in current_bowling_team:
                    if bow.player == bowl_player:
                        self.current_bowler = bow
                        existing = True
                        break

                if not existing:
                    bowler.create_bowler(bowl_player)
                    self.current_bowler = bowler
                break
        return

    def start_over(self):
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
                self.update_team_scores(score)
                self.update_current_batsman_stat(score)
                self.update_current_bowlers_state(score)
                inning_over = self.get_new_batsman(score)
                if inning_over:
                    return True
                self.change_batsman(score)
                self.show_current_batting_team_stats()
                self.show_current_bowling_team_stats()
            if self.inning == 2:
                if self.total_run_2 > self.total_run_1:
                    return True
                self.show_runs_required_to_win()
        if over.ball_count == 6:
            print('Over finished please change the bowler')
            self.previous_bowler = self.current_bowler
            self.current_bowler = None
        return False

    def start(self):
        self.select_team_for_match()
        self.toss_results()
        self.create_batting_order()

        if self.current_batting_team == self.team1:
            print("INN")
            self.inning = 1
            self.striker = self.team1_batsmen[0]
            self.non_striker = self.team1_batsmen[1]
            self.select_bowler(self.team2_bowlers)
            self.team2_bowlers.append(self.current_bowler)
            while self.total_overs_1 < self.total_overs and self.total_wicket_1 < self.total_players - 1:
                inning1_finish = self.start_over()
                if inning1_finish or self.total_overs_2 == self.total_overs:
                    break
                self.select_bowler(self.team2_bowlers)
                if self.current_bowler not in self.team2_bowlers:
                    self.team2_bowlers.append(self.current_bowler)
            self.current_batting_team = self.team2
            self.current_bowling_team = self.team1
            print('1st inning finished')

        if self.current_batting_team == self.team2:
            self.inning = 2
            self.striker = self.team2_batsmen[0]
            self.non_striker = self.team2_batsmen[1]
            self.select_bowler(self.team2_bowlers)
            self.team1_bowlers.append(self.current_bowler)
            while (self.total_overs_2 < self.total_overs and self.total_wicket_2 < self.total_players - 1 and
                   self.total_run_2 < self.total_run_1):
                inning2_finish = self.start_over()
                if inning2_finish or self.total_overs_2 == self.total_overs:
                    break
                self.select_bowler(self.team2_bowlers)
                if self.current_bowler not in self.team2_bowlers:
                    self.team1_bowlers.append(self.current_bowler)
            self.match_result()

    def show_current_batting_team_total(self):
        if self.current_batting_team == self.team1:
            print(f"{self.current_batting_team}\t\t {self.inning}")
            print(f"{self.total_run_1} - {self.total_wicket_1}\t  ({self.total_overs_1})")

        elif self.current_batting_team == self.team2:
            print(f"{self.current_batting_team}\t\t {self.inning}")
            print(f"{self.total_run_2} - {self.total_wicket_2}\t  ({self.total_overs_2})")

    def show_current_batting_team_stats(self):
        print("ID\t\t Name\t Runs\t Balls\t Fours\t Sixes\t SR")
        if self.current_batting_team == self.team1:
            for batsman in self.team1_batsmen:
                print(
                    f'{batsman.player.id}\t {batsman.player.name}\t {batsman.runs}\t\t {batsman.balls}\t\t {batsman.fours}\t\t {batsman.sixes}\t\t {batsman.strike_rate}')
                print('-------------------------------------------------')
            print(f"{self.total_run_1} - {self.total_wicket_1} ({self.total_overs_1})")
        elif self.current_batting_team == self.team2:
            for batsman in self.team2_batsmen:
                print(
                    f'{batsman.player.id}\t\t {batsman.player.name}\t {batsman.runs}\t\t {batsman.balls}\t\t {batsman.fours}\t\t {batsman.sixes}\t\t {batsman.strike_rate}')
                print('-------------------------------------------------')
            print(f"{self.total_run_2} - {self.total_wicket_2} ({self.total_overs_2})")

    def show_current_bowling_team_stats(self):
        print("ID\t\t Name\t\t Runs\t Balls\t Fours\t Sixes\t economy")
        if self.current_batting_team == self.team1:
            for bowler in self.team2_bowlers:
                print(
                    f'{bowler.player.id}\t\t {bowler.player.name}\t\t {bowler.runs}\t\t {bowler.total_balls}\t\t {bowler.four_conceded}\t\t'
                    f' {bowler.six_conceded}\t\t {bowler.economy}')
                print('-------------------------------------------------')
        elif self.current_batting_team == self.team2:
            for bowler in self.team1_bowlers:
                print(
                    f'{bowler.player.id}\t\t {bowler.player.name}\t\t {bowler.runs}\t\t {bowler.total_balls}\t\t {bowler.four_conceded}\t\t'
                    f' {bowler.six_conceded}\t\t {bowler.economy}')
                print('-------------------------------------------------')

    def update_team_scores(self, score):
        if self.current_batting_team == self.team1:

            if score in ['0', '1', '2', '3', '4', '6']:
                self.total_run_1 += int(score)
                self.total_balls_1 += 1

            elif score in ['wd', 'nb']:
                self.total_run_1 += 1
                self.team1_extras += 1

            elif score == 'out':
                self.total_wicket_1 += 1
                self.total_balls_1 += 1
            if self.total_balls_1 != 0:
                self.team1_run_rate = (self.total_run_1 * 6) / self.total_balls_1
            self.total_overs_1 = self.total_balls_1 / 6
        elif self.current_batting_team == self.team2:

            if score in ['0', '1', '2', '3', '4', '6']:
                self.total_run_2 += int(score)
                self.total_balls_2 += 1

            elif score in ['wd', 'nb']:
                self.total_run_2 += 1
                self.team2_extras += 1

            elif score == 'out':
                self.total_wicket_2 += 1
                self.total_balls_2 += 1
            if self.total_balls_2 != 0:
                self.team2_run_rate = (self.total_run_2 * 6) / self.total_balls_2
            self.total_overs_2 = self.total_balls_2 / 6

    def update_current_batsman_stat(self, score):
        if score == '4':
            self.striker.fours += 1
            self.striker.balls += 1
            self.striker.runs += 4
            self.striker.strike_rate = self.striker.runs / self.striker.balls
        elif score == '6':
            self.striker.sixes += 1
            self.striker.balls += 1
            self.striker.runs += 6
            self.striker.strike_rate = self.striker.runs / self.striker.balls
        elif score in ['0', '1', '2', '3']:
            self.striker.runs += int(score)
            self.striker.balls += 1
            self.striker.strike_rate = self.striker.runs / self.striker.balls
        elif score == 'out':
            self.striker.balls += 1
            self.striker.is_out = True

    def start_inning_select_batsman(self):
        if self.inning == 0:
            self.striker = self.team1_batsmen[0]
            self.non_striker = self.team1_batsmen[1]
        elif self.inning == 1:
            self.striker = self.team2_batsmen[0]
            self.non_striker = self.team2_batsmen[1]

    def change_batsman(self, score):
        if self.inning == 1 and self.total_wicket_1 < self.total_players - 1:
            if score in ['1', '3'] or (self.total_balls_1 != 0 and self.total_balls_1 % 6 == 0):
                self.striker, self.non_striker = self.non_striker, self.striker
        elif self.inning == 2 and self.total_wicket_2 < self.total_players - 1:
            if score in ['1', '3'] or (self.total_balls_2 != 0 and self.total_balls_2 % 6 == 0):
                self.striker, self.non_striker = self.non_striker, self.striker

    def get_new_batsman(self, score):
        if self.inning == 1:
            if score == 'out':
                if self.total_wicket_1 == self.total_players - 1:
                    return True
                self.striker = self.team1_batsmen[self.total_wicket_1]
        elif self.inning == 2:
            if score == 'out':
                if self.total_wicket_2 == self.total_players - 1:
                    return True
                self.striker = self.team2_batsmen[self.total_wicket_2]
        return False

    def update_current_bowlers_state(self, score):
        if score == '0':
            self.current_bowler.dot_balls += 1
            self.current_bowler.total_balls += 1
            self.current_bowler.economy = self.current_bowler.runs / self.current_bowler.total_balls
        elif score == 'out':
            self.current_bowler.wicket += 1
            self.current_bowler.total_balls += 1
            self.current_bowler.economy = self.current_bowler.runs / self.current_bowler.total_balls
        elif score == '4':
            self.current_bowler.runs += int(score)
            self.current_bowler.four_conceded += 1
            self.current_bowler.total_balls += 1
            self.current_bowler.economy = self.current_bowler.runs / self.current_bowler.total_balls
        elif score == '6':
            self.current_bowler.runs += int(score)
            self.current_bowler.six_conceded += 1
            self.current_bowler.total_balls += 1
            self.current_bowler.economy = self.current_bowler.runs / self.current_bowler.total_balls
        elif score == 'wd' or score == 'nb':
            self.current_bowler.runs += 1
            if self.current_bowler.total_balls != 0:
                self.current_bowler.economy = self.current_bowler.runs / self.current_bowler.total_balls
        elif score == '1' or score == '2' or score == '3':
            self.current_bowler.runs += int(score)
            self.current_bowler.total_balls += 1
            self.current_bowler.economy = self.current_bowler.runs / self.current_bowler.total_balls
        if self.current_bowler.total_balls != 0 and self.current_bowler.total_balls % 6 == 0:
            self.current_bowler.over += 1
            self.current_bowler.is_over_finished = True
        else:
            self.current_bowler.is_over_finished = False

    def show_runs_required_to_win(self):
        if self.inning == 2:
            required_run = self.total_run_1 - self.total_run_2
            balls_left = (self.total_overs * 6) - self.total_balls_2
            wickets_left = self.total_players - self.total_wicket_2 - 1
            print(f"{required_run} runs required in {balls_left} balls with {wickets_left} wickets remaining")
        else:
            return

    def match_result(self):
        if (
                self.total_overs_2 == self.total_overs or self.total_wicket_2 == self.total_players - 1) and self.total_run_2 < self.total_run_1:
            win_run = self.total_run_2 - self.total_run_1
            self.match_winner = self.team1
            print(f'{self.team1.team_name} won by {win_run} runs.')
            return
        elif (
                self.total_overs_2 == self.total_overs or self.total_wicket_2 == self.total_players - 1) and self.total_run_2 == self.total_run_1:
            print(f'Match Tied')
            return
        elif (
                self.total_overs_2 <= self.total_overs and self.total_wicket_2 < self.total_players - 1) and self.total_run_2 > self.total_run_1:
            win_wicket = self.total_players - (self.total_wicket_2 - 1)
            self.match_winner = self.team2
            print(f'{self.team2.team_name} won by {win_wicket} runs')
            return
        else:
            return
