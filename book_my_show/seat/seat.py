class Seat:
    def __init__(self):
        self.seat_id = None
        self.seat_row = None
        self.seat_type = None
        self.seat_status = None

    def get_seat_id(self):
        return self.seat_id

    def get_seat_row(self):
        return self.seat_row

    def get_seat_type(self):
        return self.seat_type

    def get_seat_status(self):
        return self.seat_status

    def set_seat_id(self, seat_id):
        self.seat_id = seat_id

    def set_seat_row(self, seat_row):
        self.seat_row = seat_row

    def set_seat_type(self, seat_type):
        self.seat_type = seat_type

    def set_seat_status(self, seat_status):
        self.seat_status = seat_status



