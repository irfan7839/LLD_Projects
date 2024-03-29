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
        self.team1 = None
        self.team2 = None
        self.team1_bowlers = []
        self.team1_extras = 0
        self.team2_extras = 0
        self.team1_batsmen = []
        self.team2_batsmen = []
        self.team2_bowlers = []
        self.total_overs_1 = None
        self.total_wicket_1 = None
        self.total_run_1 = None
        self.total_overs_2 = None
        self.total_wicket_2 = None
        self.total_run_2 = None
        self.total_run_needed = None
        self.toss_result = None
        self.current_batting_team = None
        self.current_bowling_team = None
        self.current_batting_stat = None
        self.current_bowling_stat = None
        self.current_bowler = None
        self.previous_bowler = None

    def start(self):
        while True:
            total_players = input("select number of players  ")
            if total_players.isdigit():
                break
            else:
                print("please select correct input")
                continue
        t1 = TeamImp()
        t1.create_team()
        for i in range(int(total_players)):
            p = PlayerImp()
            p.create_player(f'{t1.team_name}_0{i+1}')
            t1.add_player(p)
        self.team1 = t1
        t2 = TeamImp()
        t2.create_team()
        for i in range(int(total_players)):
            q = PlayerImp()
            q.create_player(f'{t2.team_name}_0{i+1}')
            t2.add_player(q)
        self.team2 = t2
        which_team_call = input(f"choose which team will call {t1.team_name} or {t2.team_name}")
        toss = TossImp()
        if which_team_call == t1.team_name:
            team_a = t1
            team_b = t2
        elif which_team_call == t2.team_name:
            team_a = t2
            team_b = t1
        toss.toss_time(which_team_call)

        self.toss_result = toss.toss_result()
        if self.toss_result == 'win':
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

        for player in self.team1.players_list:
            batsman = BatsmanImp()
            batsman.create_batsman(player)
            self.team1_batsmen.append(batsman)
        self.current_batting_stat = self.team1_batsmen
        self.current_bowling_stat = self.team2_bowlers
        while True:
            print("please select bowler's id from below bowlers name")
            print("ID\t Name")
            for bowler in self.current_bowling_team.players_list:
                if self.previous_bowler and self.previous_bowler.id == bowler.id:
                    continue
                else:
                    print(f"{bowler.id}\t {bowler.name}")
            bowler_id = input(f'please select bowlers id ')
            if self.previous_bowler and bowler_id == self.previous_bowler.id:
                print("one bowler can't bowl two consecutive overs")
                continue
            else:
                bowler = BowlerImp()
                bowl_player = self.current_bowling_team.get_player(bowler_id)
                bowler.create_bowler(bowl_player)
                self.current_bowler = bowl_player
                break

    def show_current_batting_team_stats(self):
        print("ID\t Name\t Runs\t Balls\t Fours\t Sixes\t SR")
        for batsman in self.current_batting_team:
            print(f'{batsman.player.id}\t {batsman.player.name}\t {batsman.runs}\t {batsman.balls}\t {batsman.fours}\t {batsman.sixes}\t {batsman.strike_rate}')
            print('-------------------------------------------------')

    def show_current_bowling_team_stats(self):
        print("ID\t Name\t Runs\t Balls\t Fours\t Sixes\t SR")
        for batsman in self.current_bowling_team:
            print(f'{batsman.player.id}\t {batsman.player.name}\t {batsman.runs}\t {batsman.balls}\t {batsman.fours}\t {batsman.sixes}\t {batsman.strike_rate}')
            print('-------------------------------------------------')
