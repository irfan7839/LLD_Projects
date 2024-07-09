import random


class Slot:
    def __init__(self):
        self.id = None
        self.start_time = None
        self.end_time = None

    def get_slot_id(self):
        return self.id


    def get_slot_start_time(self):
        return self.start_time

    def get_slot_end_time(self):
        return self.end_time

    def set_slot_id(self):
        fixed_str = 'slot_'
        numeric_part = random.randint(100, 999)
        self.id = f"{fixed_str}{numeric_part}"

    def set_slot_start_time(self, start_time):
        self.start_time = start_time

    def set_slot_end_time(self, end_time):
        self.end_time = end_time
