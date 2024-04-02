from abc import ABC, abstractmethod


class BowlingTeam(ABC):

    @abstractmethod
    def create_bowling_team(self, team_name):
        pass

    @abstractmethod
    def show_current_bowling_team_stats(self):
        pass

    @abstractmethod
    def update_current_bowling_team_stats(self, score):
        pass

    @abstractmethod
    def get_bowler_by_id(self, bowler_id):
        pass

    @abstractmethod
    def select_bowler(self):
        pass

    @abstractmethod
    def start_over(self, batting_team, bowling_team, inning):
        pass