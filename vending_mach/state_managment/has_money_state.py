from LLD_Projects.vending_mach.state_managment.dispense import DispenseState
from LLD_Projects.vending_mach.state_managment.selction_state import SelectionState
from LLD_Projects.vending_mach.state_managment.state_interface import State


class HasMoneyState(State):

    def has_money_state(self):
        print("machine is in has money state")

    def press_insert_coin_button(self, vending_machine):
        raise Exception("You can't click insert coin button in has money state")

    def insert_cash(self, vending_machine, coin):
        vending_machine.get_coin_list().append(coin)

    def select_product_button(self, vending_machine):
        vending_machine.set_vending_machine_state(SelectionState())

    def cancel_refund_button(self, vending_machine):
        print('returned the full amount')
        vending_machine.set_vending_machine_state(None)

    def choose_product(self, vending_machine, item_id):
        raise Exception("You can't choose product in has money state")

    def return_change(self, vending_machine, coin):
        raise Exception("You can't get change in has money state")

    def product_dispense(self, vending_machine, item_code):
        raise Exception("You can't dispense product in has money state")

    def refund_full_money(self):
        raise Exception("You can't get refund in has money state")
