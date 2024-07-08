from elevator_system.display.display import Display
from elevator_system.door.door import Door
from elevator_system.enums import State, Direction
from elevator_system.internal_button.internal_button import InternalButton


class ElevatorCar:

    def __init__(self):
        self.id = None
        self.current_floor = 0
        self.door = Door()
        self.display = Display()
        self.direction = Direction.UP
        self.state = State.IDLE
        self.buttons = InternalButton()

    def show_display(self):
        self.display.show_display()

    def set_display(self):
        self.display.set_display(self.current_floor, self.direction)

    def press_button(self):
        pass


