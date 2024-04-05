from abc import ABC, abstractmethod

class BankAccountInterface(ABC):


    @abstractmethod
    def create_bank_account(self, user, account_type):
        pass

    @abstractmethod
    def get_account_details(self, user):
        pass
    @abstractmethod
    def get_account_balance(self, card):
        pass
    @abstractmethod
    def deposit_money(self, amount):
        pass

    @abstractmethod
    def withdrawal_money(self, amount):
        pass

    @abstractmethod
    def add_card(self, card):
        pass

    @abstractmethod
    def get_card_details(self, card_type):
        pass
