class ItemShelf:
    def __init__(self):
        self.item = None
        self.code = None
        self.is_sold_out = False

    def set_item(self, item):
        self.item = item

    def set_code(self, code):
        self.code = code

    def set_sold_out(self, sold):
        self.is_sold_out = sold

    def get_item(self):
        return self.item

    def get_code(self):
        return self.code

    def get_sold_out(self):
        return self.is_sold_out
