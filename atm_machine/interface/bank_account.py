from abc import ABC, abstractmethod

class BankAccountInterface(ABC):


    @abstractmethod
    def create_bank_account(self, username, password, confirm_password, identity_card, dob, gender):
        pass

    @abstractmethod
    def get_account_details(self, user):
        pass
    @abstractmethod
    def get_account_balance(self, card):
        pass
    @abstractmethod
    def deposit_money(self, account_number, ifsc_code, branch_name, user_name, amount):
        pass

    @abstractmethod
    def withdrawal_money(self, bank_account, amount):
        pass
