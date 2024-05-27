from elevator_system.elevator_creator.elevator_creator import ElevatorCreator


class ExternalDispatcher:
    def __init__(self):
        self.elevator_controller_list = ElevatorCreator.elevator_controller_list

    def submit_external_request(self, floor, direction):
        for elevator_control in self.elevator_controller_list:
            elev_id = elevator_control.elevator.id
            if elev_id % 2 == 1 and floor%2 == 1:
                elevator_control.submit_external_request(floor, direction)
            if elev_id % 2 == 0 and floor % 2 == 0:
                elevator_control.submit_external_request(floor, direction)