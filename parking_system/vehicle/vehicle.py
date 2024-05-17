from enum import Enum


class VehicleType(Enum):
    TWO_WHEELER = "2w"
    THREE_WHEELER = "3w"
    FOUR_WHEELER = "4w"


class Vehicle:
    def __init__(self, v_type, v_no):
        self.vehicle_number = v_type
        self.v_type = v_no

