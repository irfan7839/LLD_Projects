from elevator_system.display.display import Display
from elevator_system.external_button.external_button import ExternalButton
from elevator_system.external_button.external_button_down import DownButton
from elevator_system.external_button.external_button_up import UpButton


class Floor:
    def __init__(self, floor_no):
        self.floor_no = floor_no
        self.up_button = None
        self.down_button = None
        self.display = Display()

    def add_up_button(self):
        self.up_button = ExternalButton()

    def add_down_button(self):
        self.down_button = ExternalButton()

    def press_up_button(self):
        self.up_button.press_button()

    def press_down_button(self):
        self.down_button.press_button()
