from LLD_Projects.vending_mach.inventory import Inventory
from LLD_Projects.vending_mach.state_managment.idle_state import IdleState


class VendingMachine:
    def __init__(self):
        self.vending_machine_state = None
        self.inventory = None
        self.coin_list = []

    def initialize_vending_machine(self, item_count):
        self.vending_machine_state = IdleState()
        self.inventory = Inventory(item_count)
        self.coin_list = []

    def get_vending_machine_state(self):
        return self.vending_machine_state

    def set_vending_machine_state(self, state):
        if not state:
            state = IdleState()
        self.vending_machine_state = state


    def get_inventory(self):
        return self.inventory

    def set_inventory(self, inventory):
        self.inventory = inventory


    def get_coin_list(self):
        return self.coin_list

    def set_coin_list(self, coin_list):
        self.coin_list = coin_list

