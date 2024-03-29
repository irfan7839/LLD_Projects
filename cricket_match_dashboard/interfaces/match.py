from abc import ABC, abstractmethod


class Matches(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def show_current_batting_team_stats(self):
        pass

    @abstractmethod
    def show_current_bowling_team_stats(self):
        pass
