# This is a sample Python script.
from parking_lot.parking_area.two_wheelers_area import TwoWheelerArea


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    parking_area = TwoWheelerArea()
    parking_area.is_slot()
    name = input('please enter Your name')
    milage = int(input("please enter Your vehicle's milage"))
    capacity = int(input("please enter Your vehicle's capacity"))
    width = int(input("please enter Your vehicle's width"))
    depth = int(input("please enter Your vehicle's depth"))
    number = input('please enter Your vehicle number')
    manufacturer = input('please enter Your vehicle manufacturer')
    parking_area.add_vehicle(milage, name, capacity, width, depth, number, manufacturer)
    parking_area.get_vehicle('two_w_000')
    parking_area.take_vehicle_out('two_w_000')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
