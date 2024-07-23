from LLD_Projects.book_my_show.user.user_interface import User


class Customer(User):
    def get_user_name(self):
        return self.name

    def get_user_age(self):
        return self.age

    def get_user_gender(self):
        return self.gender

    def get_user_city(self):
        return self.city

    def set_user_name(self, name):
        self.name = name

    def set_user_age(self, age):
        self.age = age

    def set_user_gender(self, gender):
        self.gender = gender

    def set_user_city(self, city):
        self.city = city
