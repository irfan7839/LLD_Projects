from abc import ABC, abstractmethod


class Toss(ABC):
    @abstractmethod
    def toss_time(self):
        pass

    @abstractmethod
    def toss_result(self):
        pass
