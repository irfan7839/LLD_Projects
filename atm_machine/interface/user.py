from abc import ABC, abstractmethod

class UserInterFace(ABC):

    @abstractmethod
    def get_user_details(self):
        pass

    @abstractmethod
    def create_user_details(self, username, password, dob, gender, identity, phone, email):
        pass
