from abc import ABC, abstractmethod

class AdminInterface(ABC):

    @abstractmethod
    def create_admin(self, username, password, dob, gender, identity, phone, email):
        pass

    @abstractmethod
    def get_admin_details(self):
        pass
