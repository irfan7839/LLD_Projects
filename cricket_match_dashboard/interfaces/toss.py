from abc import ABC, abstractmethod


class Toss(ABC):
    @abstractmethod
    def toss_time(self, team_name):
        pass

    @abstractmethod
    def toss_result(self):
        pass
