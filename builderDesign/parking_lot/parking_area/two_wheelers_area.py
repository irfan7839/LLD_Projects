import datetime
from datetime import timedelta

from parking_lot.parking_area.bike import Bike
from parking_lot.parking_area.bike_slot import BikeSlot


class TwoWheelerArea:
    def __init__(self):
        self.number = 10
        self.top = -1
        self.initial_charge = 20
        self.extra_charge = 100
        self.slots = {}
        for i in range(self.number):
            slot_number = f'two_w_00{i}'
            self.slots[slot_number] = None

    def is_slot(self):
        if self.top == self.number - 1:
            print(self.slots, self.number)
            print('No slot available')
            return False
        print(self.slots, self.number)
        print("Slot is available to park")
        return True

    def get_vehicle(self, slot_number):
        return self.slots[slot_number]

    def add_vehicle(self, milage, name, capacity, width, depth, number, manufacturer):

        if self.is_slot():
            bike = Bike()
            bike.create_bike_details(milage, name, capacity, width, depth, number, manufacturer)
            bike_slot = BikeSlot()
            bike_slot.create_bike_slot(bike, name, self.initial_charge, self.extra_charge)
            slot_number = f'two_w_00{self.top + 1}'
            self.slots[slot_number] = bike_slot
            self.top += 1
            print(f'your vehicle parked successfully, slot number {slot_number}')
        else:
            print('No Space is available')

    def take_vehicle_out(self, slot_number):
        val = self.slots[slot_number]
        total_amount, total_hour = val.total_cost()
        print(f'Vehicle number {val.bike.number} was parked for {total_hour} hours please pay {total_amount}')
        self.slots[slot_number] = None
