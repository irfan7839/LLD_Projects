from concrete_class.player_imp import PlayerImp
from concrete_class.team_imp import TeamImp
from concrete_class.overs_imp import OversImp
from concrete_class.toss_imp import TossImp
from interfaces.match import Matches


class MatchImp(Matches):

    def __init__(self):
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

    def start(self):
        t1 = TeamImp()
        t1.create_team()
        for i in range(int(t1.total_players)):
            p = PlayerImp()
            p.create_player(f'{t1.team_name}_0{i}')
            t1.add_player(p)
        self.team1 = t1
        t2 = TeamImp()
        t2.create_team()
        for i in range(int(t2.total_players)):
            q = PlayerImp()
            q.create_player(f'{t2.team_name}_0{i}')
            t2.add_player(q)
        self.team2 = t2
        toss = TossImp()
        toss.toss_time()
        self.toss_result = toss.toss_result()
        t1.get_all_players()
