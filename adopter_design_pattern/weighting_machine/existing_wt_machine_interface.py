from abc import ABC, abstractmethod


class WeightMachineInterface(ABC):
    @abstractmethod
    def get_weight(self):
        pass

    @abstractmethod
    def set_weight(self, weight):
        pass
