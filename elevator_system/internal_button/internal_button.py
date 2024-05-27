from elevator_system.dispatcher.internal_dispatcher import InternalDispatcher


class InternalButton:
    def __init__(self):
        self.press = False
        self.dispatcher = InternalDispatcher()
        self.buttons = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def press_button(self, floor, elevator_car):
        self.dispatcher.submit_internal_request(floor, elevator_car)

