from abc import ABC, abstractmethod


class Player(ABC):
    @abstractmethod
    def create_player(self, player_id):
        pass

    @abstractmethod
    def print_detail(self):
        pass
