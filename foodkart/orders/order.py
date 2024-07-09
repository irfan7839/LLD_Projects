from random import random, randrange


class Order:
    def __init__(self):
        self.restaurant = None
        self.order_id = None
        self.total_quantity = 0
        self.total_price = 0
        self.order_status = None

    def get_restaurant_details(self):
        return self.restaurant

    def get_order_id(self):
        return self.order_id

    def get_total_quantity(self):
        return self.total_quantity

    def get_total_price(self):
        return self.total_price

    def get_order_status(self):
        return self.order_status

    def set_restaurant_details(self, restaurant):
        self.restaurant = restaurant

    def set_order_id(self):
        order_no = randrange(0, 999)
        self.order_id = order_no

    def set_total_quantity(self, total_quantity):
        self.total_quantity = total_quantity

    def set_total_price(self):
        self.total_price = self.restaurant.price * self.total_quantity

    def set_order_status(self, status):
        self.order_status = status

