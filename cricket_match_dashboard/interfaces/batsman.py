from abc import ABC, abstractmethod


class Batsman(ABC):

    @abstractmethod
    def create_batsman(self, player):
        pass

    @abstractmethod
    def update_runs(self, score):
        pass
