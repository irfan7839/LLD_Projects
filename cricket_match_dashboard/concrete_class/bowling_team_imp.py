from LLD_Projects.cricket_match_dashboard.concrete_class.bowler_imp import BowlerImp
from LLD_Projects.cricket_match_dashboard.concrete_class.overs_imp import OversImp
from LLD_Projects.cricket_match_dashboard.interfaces.bowling_team import BowlingTeam


class BowlingTeamImp(BowlingTeam):

    def __init__(self):
        self.team = None
        self.bowlers_list = []
        self.extras = []
        self.run_conceded = 0
        self.four_conceded = 0
        self.six_concede = 0
        self.wicket_taken = 0
        self.overs_bowl = 0
        self.maiden = 0
        self.dot_balls = 0
        self.total_balls = 0
        self.current_bowler = None
        self.previous_bowler = None
        self.first_inning_score = 0

    def create_bowling_team(self, team_name):
        self.team = team_name

    def get_bowler_by_id(self, bowler_id):
        for bowler in self.bowlers_list:
            if bowler.player.id == bowler_id:
                return bowler

    def select_bowler(self):
        while True:
            print("please select bowler's id from below bowlers name")
            print("ID\t Name")
            bowling_ids = []
            self.previous_bowler = self.current_bowler
            for bowler in self.team.players_list:
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
                bowl_player = self.team.get_player(bowler_id)
                existing = False
                for bow in self.bowlers_list:
                    if bow.player == bowl_player:
                        self.current_bowler = bow
                        return bow

                if not existing:
                    bowler.create_bowler(bowl_player)
                    self.bowlers_list.append(bowler)
                    self.current_bowler = bowler

                    return bowler


    def update_current_bowling_team_stats(self, score):
        if score == '0':
            self.current_bowler.dot_balls += 1
            self.current_bowler.total_balls += 1
            self.dot_balls += 1
            self.total_balls += 1
            self.current_bowler.economy = round((self.current_bowler.runs * 6 / self.current_bowler.total_balls), 2)
        elif score == 'out':
            self.current_bowler.wicket += 1
            self.current_bowler.dot_balls += 1
            self.current_bowler.total_balls += 1
            self.wicket_taken += 1
            self.dot_balls += 1
            self.current_bowler.economy = round((self.current_bowler.runs * 6 / self.current_bowler.total_balls), 2)
        elif score == '4':
            self.current_bowler.runs += int(score)
            self.current_bowler.four_conceded += 1
            self.current_bowler.total_balls += 1
            self.run_conceded += int(score)
            self.four_conceded += 1
            self.total_balls += 1
            self.current_bowler.economy = round((self.current_bowler.runs * 6 / self.current_bowler.total_balls), 2)
        elif score == '6':
            self.current_bowler.runs += int(score)
            self.current_bowler.six_conceded += 1
            self.current_bowler.total_balls += 1
            self.run_conceded += int(score)
            self.six_concede += 1
            self.total_balls += 1
            self.current_bowler.economy = round((self.current_bowler.runs * 6 / self.current_bowler.total_balls), 2)
        elif score == 'wd' or score == 'nb':
            self.current_bowler.runs += 1
            self.extras += 1
            self.run_conceded += 1
            if self.current_bowler.total_balls != 0:
                self.current_bowler.economy = round((self.current_bowler.runs * 6 / self.current_bowler.total_balls), 2)
        elif score == '1' or score == '2' or score == '3':
            self.current_bowler.runs += int(score)
            self.current_bowler.total_balls += 1
            self.total_balls += 1
            self.run_conceded += int(score)
            self.current_bowler.economy = round((self.current_bowler.runs * 6 / self.current_bowler.total_balls), 2)
        if self.current_bowler.total_balls != 0 and self.current_bowler.total_balls % 6 == 0:
            self.current_bowler.over += 1
            self.current_bowler.is_over_finished = True
        else:
            self.current_bowler.is_over_finished = False

    def show_current_bowling_team_stats(self):
        print("ID\t\t Name\t\t Runs\t Balls\t Wickets\t Fours\t Sixes\t economy")
        for bowler in self.bowlers_list:
            print(
                f'{bowler.player.id}\t\t {bowler.player.name}\t\t {bowler.runs}\t\t {bowler.total_balls}\t\t {bowler.wicket}\t\t {bowler.four_conceded}\t\t'
                f' {bowler.six_conceded}\t\t {bowler.economy}')
            print('-------------------------------------------------')

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

    def start_over(self, batting_team, bowling_team, inning):
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
                if batting_team.show_total_runs() > self.run_conceded:
                    return True
        if over.ball_count == 6:
            print('Over finished please change the bowler')
            self.previous_bowler = self.current_bowler
            self.current_bowler = None
        return False
