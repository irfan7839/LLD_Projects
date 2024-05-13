from abc import ABC, abstractmethod

class UserInterFace(ABC):

    @abstractmethod
    def get_user_details(self):
        pass

    @abstractmethod
    def create_user(self):
        pass

    @abstractmethod
    def apply_for_bank_account(self, account_type, bank):
       pass

    @abstractmethod
    def apply_for_debit_card(self, card_type,bank):
       pass

    @abstractmethod
    def show_bank_balance(self, bank_customer):
        pass

    @abstractmethod
    def deposit_money(self, bank_customer):
        pass

    @abstractmethod
    def withdraw_money(self, bank_customer):
        pass

    @abstractmethod
    def transfer_money(self):
        pass


    @abstractmethod
    def get_bank_account(self, bank_customer):
        pass
