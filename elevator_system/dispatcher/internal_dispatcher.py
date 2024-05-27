from elevator_system.elevator_creator.elevator_creator import ElevatorCreator


class InternalDispatcher:
    def __init__(self):
        self.elevator_controller_list = ElevatorCreator.elevator_controller_list

    def submit_internal_request(self, floor, elevator_car):
        pass