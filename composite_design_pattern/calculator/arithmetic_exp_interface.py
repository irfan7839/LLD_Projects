from abc import ABC, abstractmethod


class ArithmeticInterface(ABC):
    @abstractmethod
    def evaluate(self):
        pass
