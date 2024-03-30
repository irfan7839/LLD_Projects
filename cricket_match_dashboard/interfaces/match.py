from abc import ABC, abstractmethod


class Matches(ABC):

    @abstractmethod
    def toss_results(self):
        pass

    @abstractmethod
    def select_team_for_match(self):
        pass

    @abstractmethod
    def create_batting_order(self):
        pass

    @abstractmethod
    def select_bowler(self, current_bowling_team):
        pass

    @abstractmethod
    def start_over(self):
        pass

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def show_current_batting_team_stats(self):
        pass

    @abstractmethod
    def show_current_bowling_team_stats(self):
        pass

    @abstractmethod
    def update_team_scores(self, score):
        pass

    @abstractmethod
    def update_current_batsman_stat(self, score):
        pass

    @abstractmethod
    def start_inning_select_batsman(self):
        pass

    @abstractmethod
    def change_batsman(self, score):
        pass

    def get_new_batsman(self, score):
        pass

    @abstractmethod
    def update_current_bowlers_state(self, score):
        pass

    @abstractmethod
    def match_result(self):
        pass
