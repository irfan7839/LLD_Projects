from item_shelf import ItemShelf


class Inventory:
    def __init__(self, item_count):
        self.inventory = [None] * item_count
        self.initial_empty_inventory()

    def get_inventory(self):
        return self.inventory

    def set_inventory(self, inventory):
        self.inventory = inventory

    def initial_empty_inventory(self):
        code = 101
        inv_size = len(self.inventory)
        for i in range(inv_size):
            shelf = ItemShelf()
            shelf.set_code(code)
            shelf.set_sold_out(True)
            code += 1
            self.inventory[i] = shelf

    def add_item_inventory(self, code_number, item):
        for shelf in self.inventory:
            if shelf.code == code_number:
                if shelf.is_sold_out:
                    shelf.item = item
                    shelf.set_sold_out(False)
                else:
                    raise Exception('already item is present, you can not add item here')

    def get_item(self, code_number):
        for shelf in self.inventory:
            if shelf.code == code_number:
                if not shelf.is_sold_out:
                    return shelf.item
                else:
                    raise Exception('item already sold')

    def update_sold_out_item(self, code_number):
        for shelf in self.inventory:
            if shelf.code == code_number:
                shelf.set_sold_out(True)
