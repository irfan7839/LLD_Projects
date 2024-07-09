import datetime

from LLD_Projects.interview_allocation_system.user.user_interface import User


class Interviewer(User):
    def __init__(self):
        super().__init__()
        self.interview_type = []
        self.available_slots = []

    def get_user_name(self):
        return self.name

    def get_user_email(self):
        return self.email

    def get_user_scheduled_interview(self):
        return self.schedule

    def get_user_interview_done(self):
        return self.finished_interview

    def get_user_id(self):
        return self.id

    def get_user_age(self):
        return self.age

    def set_user_name(self, name):
        self.name = name

    def set_user_email(self, email):
        self.email = email

    def set_user_scheduled_interview(self, interview):

        if interview.get_slot().start_date_time < datetime.datetime.now():
            for inter in self.schedule:
                if inter.get_slot() == interview.get_slot():
                    is_already_there = True
                    raise Exception('An interview is already scheduled in this slot')
            if interview.type in self.interview_type:
                self.schedule.append(interview)
                self.available_slots.remove(interview.get_slot())
            else:
                raise Exception('Interview type is not available for interviewer')
        else:
            is_already_there = False
            for inter in self.schedule:
                if inter.get_slot() == interview.get_slot():
                    is_already_there = True
                    self.schedule.remove(inter)
                    print('interview time finished')
                if not is_already_there:
                    raise Exception("can't schedule a interview for past date")

    def set_user_interview_done(self, interview):
        if interview.get_slot().end_date_time >= datetime.datetime.now():
            for inter in self.schedule:
                if inter.get_slot() == interview.get_slot():
                    is_already_there = True
                    raise Exception('An interview is already done interview slot')
            self.finished_interview.append(interview)
        else:
            raise Exception("interview didn't finished yet")

    def get_available_slots(self):
        return self.available_slots

    def add_slot(self, slot):
        if slot not in self.available_slots:
            self.available_slots.append(slot)
        else:
            raise Exception('slot is already present')

    def remove_slot(self, slot):
        if slot in self.available_slots:
            self.available_slots.remove(slot)
        else:
            raise Exception('slot already not available')

    def add_feedback_for_interview(self, interview):
        pass

    def set_user_id(self, user_id):
        self.id = user_id

    def set_user_age(self, age):
        self.age = age
