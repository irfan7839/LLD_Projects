import random

from LLD_Projects.interview_allocation_system.enum import InterviewType
from LLD_Projects.interview_allocation_system.interview.interview_interface import Interview


class JavaInterview(Interview):
    def get_interview_id(self):
        return self.interview_id

    def get_interview_type(self):
        return self.interview_type

    def get_interview_duration(self):
        return self.duration

    def get_interviewer(self):
        return self.interviewer

    def get_interviewee(self):
        return self.interviewee

    def get_interviewee_feedback(self):
        return self.interview_id

    def get_interviewer_feedback(self):
        return self.interviewer_feedback

    def get_interview_level(self):
        return self.interview_level

    def get_interview_status(self):
        return self.status

    def set_interview_id(self, id):
        self.interview_id = id

    def set_interview_type(self):
        self.interview_type = InterviewType.JAVA

    def set_interview_duration(self, duration):
        self.duration = duration

    def set_interviewer(self, interviewer):
        self.interviewer = interviewer

    def set_interviewee(self, interviewee):
        self.interviewee = interviewee

    def set_interviewee_feedback(self, interviewee_feedback):
        self.interviewee_feedback = interviewee_feedback

    def set_interviewer_feedback(self, interviewer_feedback):
        self.interviewer_feedback = interviewer_feedback

    def set_interview_level(self, interview_level):
        self.interview_level = interview_level

    def set_interview_status(self, status):
        self.status = status
