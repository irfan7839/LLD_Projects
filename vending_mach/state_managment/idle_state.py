from LLD_Projects.vending_mach.state_managment.has_money_state import HasMoneyState
from LLD_Projects.vending_mach.state_managment.state_interface import State


class IdleState(State):

    def idle_state(self, vending_machine):
        print("machine is in idle state")
        vending_machine.set_coins([])

    def press_insert_coin_button(self, vending_machine):
        vending_machine.set_vending_machine_state(HasMoneyState())

    def insert_cash(self, vending_machine, coin):
        raise Exception("You can't insert coin in idle state")

    def select_product_button(self, vending_machine):
        raise Exception("You can't press select product button in idle state")

    def cancel_refund_button(self, vending_machine):
        raise Exception("You can't click refund button in idle state")

    def choose_product(self, vending_machine, item_id):
        raise Exception("You can't press select product button in idle state")

    def return_change(self, vending_machine, coin):
        raise Exception("You can't get change in idle state")

    def product_dispense(self, vending_machine, item_code):
        raise Exception("You can't dispense product in idle state")

    def refund_full_money(self):
        raise Exception("You can't get refund in idle state")
