from abc import ABC, abstractmethod


class Bowler(ABC):

    @abstractmethod
    def create_bowler(self, player_id):
        pass

    @abstractmethod
    def update_state(self, score):
        pass

    @abstractmethod
    def change_bowler(self):
        pass
