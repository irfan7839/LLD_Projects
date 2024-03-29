from LLD_Projects.cricket_match_dashboard.interfaces.team import TeamStrategy


class TeamImp(TeamStrategy):

    def __init__(self):
        self.team_name = None
        self.total_players = 0
        self.players_list = [] * self.total_players

    def create_team(self):
        team_name = input("give team name ")
        self.team_name = team_name
        print(f"team {self.team_name} created successfully")

    def add_player(self, player):
        self.players_list.append(player)
        print(f"player name {player.name} added successfully ")

    def remove_player(self, player):
        self.players_list.remove(player)
        print(f"player name {player} removed successfully from team ")

    def get_player(self, player_id):
        for data in self.players_list:
            if player_id == data.id:
                print(data.name, data.id)
                return data

    def get_all_players(self):
        for data in self.players_list:
            print(data.name, data.id)

