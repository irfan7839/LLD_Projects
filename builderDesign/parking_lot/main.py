# This is a sample Python script.
from parking_lot.parking_area.parking_factory import Parkingfactory
from parking_lot.parking_area.vehicle_factory import VehicleFactory


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    vehicle_type = input('select your vehicle')
    vehicle = VehicleFactory.get_vehicle(vehicle_type)
    name = input('please enter Your name')
    milage = int(input("please enter Your vehicle's milage"))
    capacity = int(input("please enter Your vehicle's capacity"))
    number = input('please enter Your vehicle number')
    manufacturer = input('please enter Your vehicle manufacturer')

    vehicle.create_vehicle_details(milage, name, capacity, number, manufacturer)
    parking_area = Parkingfactory.get_parking_area(vehicle_type)
    parking_area.is_slot()

    parking_area.add_vehicle(vehicle, name)
    parking_area.get_vehicle('two_w_001')
    parking_area.take_vehicle_out('two_w_000')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
