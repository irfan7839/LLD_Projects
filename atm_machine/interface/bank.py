from abc import ABC, abstractmethod


class BankInterface(ABC):

    @abstractmethod
    def create_bank(self):
        pass

    @abstractmethod
    def add_new_account(self):
        pass

    @abstractmethod
    def get_account_details(self):
        pass
