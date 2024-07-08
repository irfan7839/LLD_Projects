from foodkart.user.user_interface import User


class RestaurantOwner(User):
    def __init__(self):
        super().__init__()
        self.restaurant = None

    def get_user_name(self):
        return self.name

    def get_user_age(self):
        return self.age

    def get_user_phone(self):
        return self.phone

    def get_user_gender(self):
        return self.gender

    def get_user_login_status(self):
        return self.is_login

    def get_restaurant_name(self):
        return self.restaurant

    def set_user_name(self, name):
        self.name = name

    def set_user_age(self, age):
        self.age = age

    def set_user_phone(self, phone):
        self.phone = phone

    def set_user_gender(self, gender):
        self.gender = gender

    def set_user_login_status(self, login):
        self.is_login = login

    def set_restaurant(self, restaurant):
        self.restaurant = restaurant
