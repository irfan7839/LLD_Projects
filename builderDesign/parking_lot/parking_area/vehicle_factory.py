from parking_lot.parking_area.bike import Bike
from parking_lot.parking_area.bus import Bus
from parking_lot.parking_area.car import Car
from parking_lot.parking_area.vehicle import Vehicle


class VehicleFactory:
    @staticmethod
    def get_vehicle(vehicle):
        if vehicle == 'bike':
            return Bike()
        elif vehicle == 'car':
            return Car()
        elif vehicle == 'bus':
            return Bus()
        else:
            return None

