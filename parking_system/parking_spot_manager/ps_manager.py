from parking_system.parking_spot.two_wheeler_spot import TwoWheelerSpot
from parking_system.vehicle.vehicle import VehicleType


class PsManager:
    def __init__(self):
        self.total_slot = 0
        self.slots = []

    def finding_parking_space(self):
        for space in self.slots:
            if space.isEmpty():
                return space






