from builderDesign.parking_lot.parking_area.bike_slot import BikeSlot
from builderDesign.parking_lot.parking_area.bus_slot import BusSlot
from builderDesign.parking_lot.parking_area.car_slot import CarSlot


class VehicleSlotFactory:
    @staticmethod
    def get_vehicle_slot(vehicle):

        if vehicle == 'bike':
            return BikeSlot()
        elif vehicle == 'car':
            return CarSlot()
        elif vehicle == 'bus':
            return BusSlot()
        else:
            return None
