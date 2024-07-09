from LLD_Projects.interview_allocation_system.interview_managemnet import ScheduleManagement
from LLD_Projects.interview_allocation_system.user.interviewer_user import Interviewer


class Main:
    @staticmethod
    def is_valid_email(email):
        if "@" in email and email.endswith(".com"):
            return True
        else:
            return False

    @staticmethod
    def start():
        while True:
            interviewer_name = input('please provide interviewer name')
            interviewer_age = input('please provide interviewer age')
            interviewer_email = input('please provide interviewer email')
            interviewer_id = input('please provide interviewer id')
            if not interviewer_age.isnumeric() or not Main.is_valid_email(interviewer_email):
                continue
            else:
                interviewer = Interviewer()
                interviewer.set_user_name(interviewer_name)
                interviewer.set_user_email(interviewer_email)
                interviewer.set_user_age(interviewer_age)
                interviewer.set_user_id(interviewer_id)
                interviewer.set_user_scheduled_interview(ScheduleManagement())
                break

        while True:
            interviewee_name = input('please provide interviewer name')
            interviewee_age = input('please provide interviewer age')
            interviewee_email = input('please provide interviewer email')
            interviewee_id = input('please provide interviewer id')
            if not interviewee_age.isnumeric() or not Main.is_valid_email(interviewee_email):
                continue
            else:
                interviewee = Interviewer()
                interviewee.set_user_name(interviewee_name)
                interviewee.set_user_email(interviewee_email)
                interviewee.set_user_age(interviewee_age)
                interviewee.set_user_id(interviewee_id)
                interviewee.set_user_scheduled_interview(ScheduleManagement())
                break
