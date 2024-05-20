from enum import Enum

from parking_system.entry_gate.entry_gate import EntryGate
from parking_system.parking_manager_factory.parking_manager_factory import PSMFactory
from parking_system.vehicle.vehicle import VehicleType


class VehiclePark(Enum):
    PARK = "park"
    UN_PARK = "un-park"
    SLOT = "slot"


vehicle_type = {'1': VehicleType.TWO_WHEELER,
                '2': VehicleType.FOUR_WHEELER
                }
parking_selection = {
    '1': VehiclePark.PARK,
    '2': VehiclePark.UN_PARK,
    '3': VehiclePark.SLOT
}


class Main:
    def __init__(self):
        self.parking_space = None
        self.v_type = ""
        self.vehicle = None

    def start(self):
        while True:
            v_type = input('select 1. for Bike 2.for car')
            if v_type in vehicle_type:
                self.parking_space = PSMFactory.get_parking_manager(vehicle_type[v_type])
                self.v_type = vehicle_type[v_type]
                while True:
                    total_slot = input('please provide total slots')
                    if total_slot.isnumeric():
                        self.parking_space.total_parking_slot(int(total_slot))
                        break
                    else:
                        continue
                break
            else:
                continue
        while True:
            inp = input('select 1. parking 2. un-parking 3. available slots')
            if inp in parking_selection:
                if inp == '1':
                    if self.parking_space.is_space_available():
                        vehicle_number = input('please provide vehicle number')
                        entry_gate = EntryGate()
                        self.vehicle = entry_gate.get_vehicle_details(self.v_type, vehicle_number)
                        entry_gate.park_vehicle()
                    else:
                        print("No slot is available")


if __name__ == '__main__':
    print('create parking area')
    main = Main()
    main.start()
