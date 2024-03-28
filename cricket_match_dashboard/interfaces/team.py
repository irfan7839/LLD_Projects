from abc import ABC, abstractmethod


class TeamStrategy(ABC):
    @abstractmethod
    def create_team(self):
        pass

    @abstractmethod
    def add_player(self, player):
        pass

    @abstractmethod
    def remove_player(self, player):
        pass

    @abstractmethod
    def get_player(self, player_id):
        pass

    @abstractmethod
    def get_all_players(self):
        pass
