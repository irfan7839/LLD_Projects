from abc import ABC, abstractmethod


class User(ABC):
    def __init__(self):
        self.name = None
        self.id = None
        self.age = None
        self.email = None
        self.schedule = None
        self.finished_interview = None

    @abstractmethod
    def get_user_name(self):
        pass

    @abstractmethod
    def get_user_email(self):
        pass

    @abstractmethod
    def get_user_id(self):
        pass

    @abstractmethod
    def get_user_age(self):
        pass

    @abstractmethod
    def get_user_scheduled_interview(self):
        pass

    @abstractmethod
    def get_user_interview_done(self):
        pass

    @abstractmethod
    def set_user_name(self, name):
        pass

    @abstractmethod
    def set_user_email(self, email):
        pass

    @abstractmethod
    def set_user_id(self, user_id):
        pass

    @abstractmethod
    def set_user_age(self, age):
        pass

    @abstractmethod
    def set_user_scheduled_interview(self, interview):
        pass

    @abstractmethod
    def set_user_interview_done(self, interview):
        pass
