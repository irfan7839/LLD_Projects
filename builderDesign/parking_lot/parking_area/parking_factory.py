from parking_lot.parking_area.four_wheelers_area import FourWheelerArea
from parking_lot.parking_area.large_vehicles_area import LargeVehicleArea
from parking_lot.parking_area.two_wheelers_area import TwoWheelerArea


class Parkingfactory:
    @staticmethod
    def get_parking_area(vehicle_type):

        if vehicle_type == 'bike':
            return TwoWheelerArea()
        elif vehicle_type == 'car':
            return FourWheelerArea()
        elif vehicle_type == 'bus':
            return LargeVehicleArea()
        else:
            return None

