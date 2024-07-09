from abc import ABC, abstractmethod


class Interview(ABC):
    def __init__(self):
        self.interview_id = None
        self.interview_type = None
        self.duration = None
        self.slot = None
        self.interviewer = None
        self.interviewee = None
        self.interviewee_feedback = None
        self.interviewer_feedback = None
        self.interview_level = None
        self.status = None

    @abstractmethod
    def get_interview_id(self):
        pass

    @abstractmethod
    def get_interview_type(self):
        pass

    @abstractmethod
    def get_interview_duration(self):
        pass

    @abstractmethod
    def get_interviewer(self):
        pass

    @abstractmethod
    def get_interviewee(self):
        pass

    @abstractmethod
    def get_interviewee_feedback(self):
        pass

    @abstractmethod
    def get_interviewer_feedback(self):
        pass

    @abstractmethod
    def get_interview_level(self):
        pass

    @abstractmethod
    def get_interview_status(self):
        pass
    @abstractmethod
    def set_interview_id(self, id):
        pass

    @abstractmethod
    def set_interview_type(self):
        pass

    @abstractmethod
    def set_interview_duration(self, duration):
        pass

    @abstractmethod
    def set_interviewer(self, interviewer):
        pass

    @abstractmethod
    def set_interviewee(self, interviewee):
        pass

    @abstractmethod
    def set_interviewee_feedback(self, interviewee_feedback):
        pass

    @abstractmethod
    def set_interviewer_feedback(self, interviewer_feedback):
        pass

    @abstractmethod
    def set_interview_level(self, interview_level):
        pass

    @abstractmethod
    def set_interview_status(self, status):
        pass
