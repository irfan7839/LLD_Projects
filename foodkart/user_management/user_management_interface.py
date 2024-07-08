from abc import ABC, abstractmethod

class UserManagement(ABC):
    def __init__(self):
        self.user_list = []

    @abstractmethod
    def get_user_list(self):
        pass

    @abstractmethod
    def update_user_list(self, user):
        pass

    @abstractmethod
    def get_user_by_phone(self, phone):
        pass
