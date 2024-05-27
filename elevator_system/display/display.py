class Display:
    def __init__(self):
        self.floor = None
        self.direction = None

    def show_display(self):
        print(self.floor)
        print(self.direction)

    def set_display(self, floor, direction):
        self.floor = floor
        self.direction = direction

