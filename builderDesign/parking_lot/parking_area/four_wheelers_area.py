from parking_lot.parking_area.car import Car
from parking_lot.parking_area.car_slot import CarSlot


class FourWheelerArea:
    def __init__(self):
        self.number = 10
        self.total_vehicle = 0
        self.initial_charge = 20
        self.extra_charge = 100
        self.slots = {}
        for i in range(self.number):
            slot_number = f'four_w_00{i+1}'
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

    def add_vehicle(self, car, name):

        if self.is_slot():
            car_slot = CarSlot()
            car_slot.create_car_slot(car, name, self.initial_charge, self.extra_charge)
            slot_number = self.is_slot()
            self.slots[slot_number] = car_slot
            self.total_vehicle += 1
            print(f'your vehicle parked successfully, slot number {slot_number}')
        else:
            print('No Space is available')

    def take_vehicle_out(self, slot_number):
        val = self.slots[slot_number]
        total_amount, total_hour = val.total_cost()
        print(f'Vehicle number {val.car.number} was parked for {total_hour} hours please pay {total_amount}')
        self.slots[slot_number] = None
        self.total_vehicle += 1
