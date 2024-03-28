from interfaces.team import TeamStrategy


class TeamImp(TeamStrategy):

    def __init__(self):
        self.team_name = None
        self.total_players = 0
        self.players_list = [] * self.total_players

    def create_team(self):
        team_name = input("give team name")
        total_players = input("give total player")
        self.team_name = team_name
        self.total_players = total_players
        print(f"team {self.team_name} with {self.total_players} total players created successfully")

    def add_player(self, player):
        self.players_list.append(player)
        print(f"player name {player.name} added successfully")

    def remove_player(self, player):
        self.players_list.remove(player)
        print(f"player name {player} removed successfully from team")

    def get_player(self, player_id):
        for data in self.players_list:
            if player_id == data.player_id:
                print(data.name, data.player_id)
                return data

    def get_all_players(self):
        for data in self.players_list:
            print(data.name, data.player_id)

