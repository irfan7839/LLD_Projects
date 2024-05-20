from parking_system.parking_spot.four_wheeler import FourWheelerSpot
from parking_system.parking_spot.two_wheeler_spot import TwoWheelerSpot
from parking_system.vehicle.vehicle import VehicleType


class PSFactory:
    @staticmethod
    def get_parking_manager(v_type):
        if v_type == VehicleType.TWO_WHEELER:
            return TwoWheelerSpot()
        elif v_type == VehicleType.FOUR_WHEELER:
            return FourWheelerSpot()
