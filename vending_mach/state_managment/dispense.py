from LLD_Projects.vending_mach.state_managment.state_interface import State


class DispenseState(State):

    def dispense_state(self):
        print("machine is in selection state")

    def press_insert_coin_button(self, vending_machine):
        raise Exception("You can't click insert coin button in dispense state")

    def insert_cash(self, vending_machine, coin):
        raise Exception("You can't  insert coin in dispense state")

    def select_product_button(self, vending_machine):
        raise Exception("You can't click select product button in dispense state")

    def cancel_refund_button(self, vending_machine):
        raise Exception("You can't click select product button in dispense state")

    def choose_product(self, vending_machine, item_id):
        raise Exception("You can't click select product button in dispense state")

    def return_change(self, vending_machine, coins):
        raise Exception("You can't click select product button in dispense state")

    def product_dispense(self, vending_machine, item_code):
        item = vending_machine.get_inventory().get_item(item_code)
        vending_machine.get_inventory().update_sold_out_item(item_code)
        vending_machine.set_vending_machine_state(None)
        return item

    def refund_full_money(self):
        raise Exception("You can't get refund in selection state")
