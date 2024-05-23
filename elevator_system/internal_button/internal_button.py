class InternalButton:
    def __init__(self):
        self.press = False

    def press_button(self):
        self.press = True

    def clear_button(self):
        self.press = False