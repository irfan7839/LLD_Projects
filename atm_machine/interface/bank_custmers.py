from abc import ABC, abstractmethod


class BankCustomersInterface(ABC):

    @abstractmethod
    def add_bank_customer(self, bank_account):
        pass

    @abstractmethod
    def get_bank_customer(self, account_number):
        pass

    @abstractmethod
    def activate_bank_customer(self, account_number):
        pass

    @abstractmethod
    def deactivate_bank_customer(self, account_number):
        pass
