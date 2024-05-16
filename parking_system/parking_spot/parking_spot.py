import enum


class ParkingSpot:
    def __init__(self):
        self.id = ''
        self.vehicle = None
        self.price = 0
        self.isEmpty = True

    def assign_price(self):
        self.price = 10

    def assign_spot_id(self, s_id, v_type: str):
        self.id = v_type + '_00' + s_id

    def park_vehicle(self, vehicle):
        self.vehicle = vehicle
        self.isEmpty = False

    def remove_vehicle(self):
        self.vehicle = None
        self.isEmpty = True
