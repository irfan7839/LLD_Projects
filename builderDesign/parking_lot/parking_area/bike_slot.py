import datetime
import math


class BikeSlot:
    def __init__(self):
        self.slot_number = ''
        self.initial_charge = 0
        self.extra_charge = 0

        self.start_time = datetime.datetime.now()
        self.end_time = None
        self.actual_end_time = ''
        self.total_amount = 0
        self.bike = None
        self.owner_name = ''

    def create_bike_slot(self, bike, owner_name, charge, extra_charge):
        self.bike = bike
        self.initial_charge = charge
        self.extra_charge = extra_charge
        self.owner_name = owner_name

    def update_slot_number(self, slot_number):
        self.slot_number = slot_number

    def total_cost(self):
        total_hour = self.get_total_hour()
        total_cost = 0
        total_cost += self.initial_charge
        total_cost += ((total_hour - 1) * self.extra_charge)
        return total_hour, total_cost

    def get_total_hour(self):
        current_time = datetime.datetime.now()
        time_difference = current_time - self.start_time
        td_hour = time_difference.total_seconds() / 3600
        total_hour = math.ceil(td_hour)
        return total_hour


