

from LLD_Projects.vending_mach.enum_fn import Coin, ItemType
from LLD_Projects.vending_mach.item import Item
from LLD_Projects.vending_mach.vending_machine import VendingMachine


class Main:
    @staticmethod
    def start():
        item_count = input('please select size of inventory')
        vending_machine = VendingMachine()
        vending_machine.initialize_vending_machine(int(item_count))
        try:
            print("filling up the inventory")
            Main.filling_up_inventory(vending_machine)
            Main.display_inventory(vending_machine)

            print('clicking on insert button')
            vending_state = vending_machine.get_vending_machine_state()
            vending_state.press_insert_coin_button(vending_machine)

            vending_state = vending_machine.get_vending_machine_state()
            print(f'vending machine is in {vending_state}, please insert coins!')
            vending_state.insert_cash(vending_machine, Coin.NICKEL)
            vending_state.insert_cash(vending_machine, Coin.QUARTER)

            print('clicking on product selection button')
            vending_state.select_product_button(vending_machine)

            vending_state = vending_machine.get_vending_machine_state()
            vending_state.choose_product(vending_machine, 102)
            Main.display_inventory(vending_machine)

        except Exception as e:
            print(e)

    @staticmethod
    def filling_up_inventory(vending_machine):
        slots = vending_machine.get_inventory().get_inventory()
        for i in range(len(slots)):
            item = Item()
            if i <= 3:
                item.set_type(ItemType.COKE)
                item.set_price(12)
            elif 3 < i <= 6:
                item.set_type(ItemType.PEPSI)
                item.set_price(15)

            elif 6 < i <= 9:
                item.set_type(ItemType.SODA)
                item.set_price(15)
            else:
                item.set_type(ItemType.JUICE)
                item.set_price(20)

            slots[i].set_item(item)
            slots[i].set_sold_out(False)

    @staticmethod
    def display_inventory(vending_machine):
        slots = vending_machine.get_inventory().get_inventory()
        for i in range(len(slots)):
            print(f'Code: {slots[i].get_code()},'
                  f' Name: {slots[i].get_item().get_type()}, '
                  f'Price: {slots[i].get_item().get_price()}, isAvailable:{not slots[i].get_sold_out()} ')


main = Main()
main.start()