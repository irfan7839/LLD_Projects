from abc import ABC, abstractmethod

class Matches(ABC):

    @abstractmethod
    def create_batsman(self):
        pass

    @abstractmethod
    def create_bowler(self):
        pass

    @abstractmethod
    def start(self):
        pass