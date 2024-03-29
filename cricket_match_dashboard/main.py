from concrete_class.player_imp import PlayerImp
from concrete_class.team_imp import TeamImp
from concrete_class.overs_imp import OversImp
from concrete_class.toss_imp import TossImp
from  concrete_class.match_imp import MatchImp


if __name__ == '__main__':
    m1 = MatchImp()
    m1.start()
    # t1 = TeamImp()
    # t1.create_team()
    # for i in range(int(t1.total_players)):
    #     p = PlayerImp()
    #     p.create_player()
    #     t1.add_player(p)
    # t2 = TeamImp()
    # t2.create_team()
    # for i in range(int(t2.total_players)):
    #     q = PlayerImp()
    #     q.create_player()
    #     t2.add_player(q)
    # toss = TossImp()
    # toss.toss_time()
    # toss.toss_result()
    # t1.get_players()
