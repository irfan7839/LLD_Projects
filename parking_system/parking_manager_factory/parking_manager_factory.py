from parking_system.parking_spot_manager.Two_wheeler_ps_manager import TwoWheelerPsManager
from parking_system.parking_spot_manager.four_wheeler_ps_manager import FourWheelerPsManager
from parking_system.vehicle.vehicle import VehicleType


class PSMFactory:
    @staticmethod
    def get_parking_manager(v_type):
        if v_type == VehicleType.TWO_WHEELER:
            return TwoWheelerPsManager()
        elif v_type == VehicleType.FOUR_WHEELER:
            return FourWheelerPsManager()
