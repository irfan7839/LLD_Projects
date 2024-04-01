from LLD_Projects.cricket_match_dashboard.interfaces.batting_team import BattingTeam


class BattingTeamImp(BattingTeam):
    def __init__(self):
        self.total_players = 0
        self.team = None
        self.batsman = []
        self.total_overs = 0
        self.total_wicket = 0
        self.total_run = 0
        self.total_balls = 0
        self.total_run_rate = 0
        self.total_extras = 0
        self.striker = None
        self.non_striker = None

    def create_batting_team(self, team, batsman_list, total_players):
        self.team = team
        self.total_players = total_players
        self.batsman = batsman_list

    def update_team_scores(self, score):

        if score in ['0', '1', '2', '3', '4', '6']:
            self.total_run += int(score)
            self.total_balls += 1

        elif score in ['wd', 'nb']:
            self.total_run += 1
            self.total_extras += 1

        elif score == 'out':
            self.total_wicket += 1
            self.total_balls += 1
        if self.total_balls != 0:
            self.total_run_rate = (self.total_run * 6) / self.total_balls
        self.total_overs = self.total_balls / 6

    def get_new_batsman(self, score):
        if score == 'out':
            if self.total_wicket == self.total_players - 1:
                return True
            self.striker = self.batsman[self.total_wicket]
        return False

    def change_batsman(self, score):
        if self.total_wicket < self.total_players - 1:
            if score in ['1', '3'] or (self.total_balls != 0 and self.total_balls % 6 == 0):
                self.striker, self.non_striker = self.non_striker, self.striker

    def start_inning_select_batsman(self):
        self.striker = self.batsman[0]
        self.non_striker = self.batsman[1]

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

    def show_current_batting_team_stats(self):
        print("ID\t\t Name\t Runs\t Balls\t Fours\t Sixes\t SR")
        for batsman in self.batsman:
            print(
                f'{batsman.player.id}\t {batsman.player.name}\t {batsman.runs}\t\t {batsman.balls}\t\t {batsman.fours}\t\t {batsman.sixes}\t\t {batsman.strike_rate}')
            print('-------------------------------------------------')
        print(f"{self.total_run} - {self.total_wicket} ({self.total_overs})")

    def show_total_runs(self):
        return self.total_run

    def show_total_wickets(self):
        return self.total_wicket

    def show_total_overs(self):
        return self.total_overs

    def show_runs_required(self, inning, bt1):
        if inning == 2:
            required_run = bt1.total_run - self.total_run
            balls_left = (self.total_overs * 6) - self.total_balls
            wickets_left = self.total_players - self.total_wicket - 1
            print(f"{required_run} runs required in {balls_left} balls with {wickets_left} wickets remaining")
