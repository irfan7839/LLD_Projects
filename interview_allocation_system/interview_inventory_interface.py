from abc import ABC, abstractmethod


class InterviewInventory(ABC):
    def __init__(self):
        self.inventory = []

    @abstractmethod
    def fill_inventory(self, interview):
        pass
