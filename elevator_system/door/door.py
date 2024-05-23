class Door:
    def __init__(self):
        self.is_open = False

    def open_door(self):
        if not self.is_open:
            self.is_open = True
            print('Door opened')
        print('door already open')

    def close_door(self):
        if self.is_open:
            self.is_open = False
            print('Door closed')
        print('door already closed')
