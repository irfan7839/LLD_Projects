from elevator_system.internal_button.internal_button import InternalButton


class ElevatorCar:

    def __init__(self, no_of_floors):
        self.current_floor = None
        self.door = None
        self.display = None
        self.direction = None
        self.status = None
        self.buttons = {'open_door': InternalButton(), 'close_door': InternalButton()}

        for i in range(no_of_floors+1):
            self.buttons[i] = InternalButton()
