from abc import ABC, abstractmethod


class User(ABC):
    def __init__(self):
        self.name = None
        self.gender = None
        self.age = None
        self.city = None

    @abstractmethod
    def get_user_name(self):
        pass

    @abstractmethod
    def get_user_age(self):
        pass

    @abstractmethod
    def get_user_gender(self):
        pass

    @abstractmethod
    def get_user_city(self):
        pass

    @abstractmethod
    def set_user_name(self, name):
        pass

    @abstractmethod
    def set_user_age(self, age):
        pass

    @abstractmethod
    def set_user_gender(self, gender):
        pass

    @abstractmethod
    def set_user_city(self, city):
        pass
