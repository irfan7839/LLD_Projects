from LLD_Projects.null_object_pattern.car import Car
from LLD_Projects.null_object_pattern.null_object import NullObject


class VehicleFactory:

    def get_vehicle(self, vehicle_type):
        if vehicle_type == 'CAR':
            return Car()
        return NullObject()
