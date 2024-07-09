class ScheduleManagement:
    def __init__(self):
        self.interview_list = []

    def get_interview_list(self):
        return self.interview_list

    def get_interview_by_id(self, int_id):
        for interview in self.interview_list:
            if int_id == interview.interview_id:
                return interview
        raise Exception('No interview is scheduled with this id')

    def add_interview(self, interview):
        if len(self.interview_list) < 2:
            self.interview_list.append(interview)
        else:
            raise Exception('You can only schedule two interview')

    def remove_schedule_interview(self, interview_id):
        for interview in self.interview_list:
            if interview_id == interview.interview_id:
                self.interview_list.remove(interview)
                return
        raise Exception('No interview is scheduled with this id')

