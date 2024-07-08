from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self):
        self.name = None
        self.age = None
        self.gender = None
        self.phone = None
        self.is_login = False

    @abstractmethod
    def get_user_name(self):
        pass

    @abstractmethod
    def get_user_age(self):
        pass
    @abstractmethod
    def get_user_phone(self):
        pass
    @abstractmethod
    def get_user_gender(self):
        pass
    @abstractmethod
    def get_user_login_status(self):
        pass

    @abstractmethod
    def set_user_name(self, name):
        pass

    @abstractmethod
    def set_user_age(self, age):
        pass

    @abstractmethod
    def set_user_phone(self, phone):
        pass

    @abstractmethod
    def set_user_gender(self, gender):
        pass

    @abstractmethod
    def set_user_login_status(self, login):
        pass
