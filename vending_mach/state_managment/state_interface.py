from abc import ABC, abstractmethod
class State(ABC):

    @abstractmethod
    def press_insert_coin_button(self, vending_machine):
        pass

    @abstractmethod
    def insert_cash(self, vending_machine, coin):
        pass

    @abstractmethod
    def select_product_button(self, vending_machine):
        pass

    @abstractmethod
    def cancel_refund_button(self, vending_machine):
        pass

    @abstractmethod
    def choose_product(self, vending_machine, item_id):
        pass

    @abstractmethod
    def return_change(self, vending_machine, coin):
        pass

    @abstractmethod
    def product_dispense(self, vending_machine, item_code):
        pass

    @abstractmethod
    def refund_full_money(self):
        pass

