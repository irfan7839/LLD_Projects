from abc import ABC, abstractmethod


class BattingTeam(ABC):

    @abstractmethod
    def create_batting_team(self, team, batsman_list, total_players):
        pass

    @abstractmethod
    def update_team_scores(self, score):
        pass

    @abstractmethod
    def get_new_batsman(self, score):
        pass

    @abstractmethod
    def start_inning_select_batsman(self):
        pass

    @abstractmethod
    def update_current_batsman_stat(self, score):
        pass

    @abstractmethod
    def show_current_batting_team_stats(self):
        pass

    @abstractmethod
    def show_total_runs(self):
        pass

    @abstractmethod
    def show_total_wickets(self):
        pass

    @abstractmethod
    def show_total_overs(self):
        pass

    @abstractmethod
    def show_runs_required(self, inning, bt1):
        pass

