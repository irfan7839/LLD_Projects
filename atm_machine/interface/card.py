from abc import ABC, abstractmethod


class CardInterface(ABC):

    @abstractmethod
    def create_card(self, card_type, name):
        pass

    @abstractmethod
    def get_card_number(self):
        pass

    @abstractmethod
    def get_expiry(self):
        pass

    @abstractmethod
    def get_cvv(self):
        pass

    @abstractmethod
    def add_account_number(self, account_number):
        pass

