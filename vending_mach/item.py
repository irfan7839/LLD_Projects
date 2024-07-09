class Item:
    def __init__(self):
        self._item_name = None
        self._item_price = None

    def get_type(self):
        return self._item_name

    def set_type(self, name):
        self._item_name = name

    def get_price(self):
        return self._item_price

    def set_price(self, price):
        self._item_price = price
