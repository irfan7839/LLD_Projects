import datetime
from datetime import timedelta

from parking_lot.parking_area.bike import Bike
from parking_lot.parking_area.bike_slot import BikeSlot


class TwoWheelerArea:
    def __init__(self):
        self.number = 10
        self.total_vehicles = 0
        self.initial_charge = 20
        self.extra_charge = 100
        self.slots = {}
        for i in range(self.number):
            slot_number = f'two_w_00{i}'
            self.slots[slot_number] = None

    def is_slot(self):
        for slot in self.slots:
            if self.slots[slot] is None:
                print("Slot is available to park")
                return slot
        print("Slot is not available to park")
        return None

    def get_vehicle(self, slot_number):
        return self.slots[slot_number]

    def add_vehicle(self, bike, name):

        if self.is_slot():

            bike_slot = BikeSlot()
            bike_slot.create_bike_slot(bike, name, self.initial_charge, self.extra_charge)
            slot_number = self.is_slot()
            self.slots[slot_number] = bike_slot
            self.total_vehicles += 1
            print(f'your vehicle parked successfully, slot number {slot_number}')
        else:
            print('No Space is available')

    def take_vehicle_out(self, slot_number):
        val = self.slots[slot_number]
        total_hour, total_amount, = val.total_cost()
        self.total_vehicles -= 1
        print(f'Vehicle number {val.bike.number} was parked for {total_hour} hours please pay {total_amount}')
        self.slots[slot_number] = None
