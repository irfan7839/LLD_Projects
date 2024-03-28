from abc import ABC, abstractmethod


class Overs(ABC):
    @abstractmethod
    def add_ball_update(self, score):
        pass

    @abstractmethod
    def total_score_in_over(self):
        pass

    @abstractmethod
    def clear_over(self):
        pass

    @abstractmethod
    def show_no_of_balls(self):
        pass
