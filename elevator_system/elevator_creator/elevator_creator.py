from elevator_system.elevator_controller.elevator_controller import ElevatorController
from elevator_system.evelator_car.elevation_car import ElevatorCar


class ElevatorCreator:
    elevator_controller_list = []
    def __init__(self):
        self.elevator_controller_list = []

    def add_elevators(self):
        elevator1 = ElevatorCar()
        elevator1.id = 1
        elevator1_controller = ElevatorController(elevator1)
        elevator2 = ElevatorCar()
        elevator2.id = 2
        elevator2_controller = ElevatorController(elevator2)
        self.elevator_controller_list.append(elevator1_controller)
        self.elevator_controller_list.append(elevator2_controller)

