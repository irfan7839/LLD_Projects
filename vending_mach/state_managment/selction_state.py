from LLD_Projects.vending_mach.state_managment.dispense import DispenseState
from LLD_Projects.vending_mach.state_managment.state_interface import State


class SelectionState(State):

    def selection_state(self):
        print("machine is in selection state")

    def press_insert_coin_button(self, vending_machine):
        raise Exception("You can't click insert coin button in selection state")

    def insert_cash(self, vending_machine, coin):
        raise Exception("You can't  insert coin in selection state")

    def select_product_button(self, vending_machine):
        raise Exception("You can't click select product button in selection state")

    def cancel_refund_button(self, vending_machine):
        print('returned the full amount')
        vending_machine.set_vending_machine_state(None)

    def choose_product(self, vending_machine, item_id):
        item = vending_machine.get_inventory().get_item(item_id)
        amount = 0
        coins = vending_machine.get_coin_list()
        for coin in coins:
            amount += coin.value

        if amount < item._item_price:
            print('Insufficient amount')
            self.refund_full_money()
            vending_machine.set_vending_machine_state(None)
            raise Exception("Insufficient amount")
        elif amount >= item._item_price:
            if amount > item._item_price:
                self.return_change(vending_machine, coins)
        vending_machine.set_vending_machine_state(DispenseState())

    def return_change(self, vending_machine, coins):
        # vending_machine.get_change(coins)
        print(f'please collect {coins} from the trey ')

    def product_dispense(self, vending_machine, item_code):
        raise Exception("You can't dispense product in selection state")

    def refund_full_money(self):
        raise Exception("You can't get refund in selection state")
