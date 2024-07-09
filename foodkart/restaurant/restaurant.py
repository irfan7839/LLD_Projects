class Restaurant:
    def __init__(self):
        self.restaurant_name = None
        self.restaurant_id = None
        self.specialized_food = None
        self.initial_quantity = 0
        self.price = None
        self.rating_list = []
        self.avg_rating = 0
        self.pin_list = []

    def get_restaurant_name(self):
        return self.restaurant_name

    def get_restaurant_id(self):
        return self.restaurant_id

    def get_restaurant_food(self):
        return self.specialized_food

    def get_food_price(self):
        return self.price

    def get_pin_list(self):
        return self.pin_list

    def get_initial_quantity(self):
        return self.initial_quantity

    def get_avg_rating(self):
        return self.avg_rating

    def get_restaurant_ratings(self):
        return self.rating_list

    def set_restaurant_name(self, name):
        self.restaurant_name = name

    def set_restaurant_id(self, res_id):
        self.restaurant_id = res_id

    def set_restaurant_food(self, food):
        self.specialized_food = food

    def set_food_price(self, price):
        self.price = price

    def set_initial_quantity(self, quantity):
        self.initial_quantity = quantity

    def set_restaurant_ratings(self, rating):
        l = len(self.rating_list)
        self.avg_rating = ((l * self.avg_rating) + rating.star) / (l + 1)
        self.rating_list.append(rating)

    def add_pin_code_list(self, pincode):
        for pin in self.pin_list:
            if pin == pincode:
                print(f'pincode {pincode} already exist!')
                return
        self.pin_list.append(pincode)