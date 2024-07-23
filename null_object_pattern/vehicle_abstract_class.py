from abc import ABC, abstractmethod


class VehicleAbstract(ABC):

    @abstractmethod
    def get_capacity(self):
        pass
    @abstractmethod
    def get_seats(self):
        pass