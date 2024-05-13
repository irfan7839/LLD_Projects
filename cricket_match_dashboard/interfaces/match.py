from abc import ABC, abstractmethod


class Matches(ABC):

    @abstractmethod
    def toss_results(self):
        pass

    @abstractmethod
    def select_team_for_match(self):
        pass

    @abstractmethod
    def show_runs_required_to_win(self):
        pass

    @abstractmethod
    def start_match(self):
        pass

    @abstractmethod
    def start_over(self, batsman, bowler):
        pass

    @abstractmethod
    def match_result(self):
        pass
