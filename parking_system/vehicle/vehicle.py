from enum import Enum


class VehicleType(Enum):
    TWO_WHEELER = "2w"
    THREE_WHEELER = "3w"
    FOUR_WHEELER = "4w"


class Vehicle:
    def __init__(self, v_no, v_type):
        self.vehicle_number = v_no
        if isinstance(v_type, VehicleType):
            self.v_type = v_type
        else:
            raise ValueError("Invalid vehicle type")
