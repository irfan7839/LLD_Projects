from parking_system.parking_spot.two_wheeler_spot import TwoWheelerSpot
from parking_system.parking_spot_manager.ps_manager import PsManager
from parking_system.vehicle.vehicle import VehicleType


class TwoWheelerPsManager(PsManager):
    def total_parking_slot(self, slot):
        self.total_slot = slot
        self.slots = [None] * self.total_slot
        self.spot = TwoWheelerSpot()
        for i in range(self.total_slot):
            self.slots[i] = self.spot.assign_spot_id(i + 1, VehicleType.TWO_WHEELER)

    def add_parking_space(self, size):
        for i in range(size):
            self.slots[self.total_slot + i] = self.spot.assign_spot_id(self.total_slot + i + 1, VehicleType.TWO_WHEELER)

        self.total_slot += size

    def is_space_available(self):
        for slot in self.slots:
            if slot.isEmpty:
                return True
        return False


