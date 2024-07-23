class Booking:
    def __init__(self):
        self.booking_id = None
        self.show = None
        self.seat_list = []
        self.payment = None
        self.total_price = None

    def get_booking_id(self):
        return self.booking_id

    def get_show(self):
        return self.show

    def get_seat_list(self):
        return self.seat_list

    def get_payment_details(self):
        return self.payment

    def set_booking_id(self, booking_id):
        self.booking_id = booking_id

    def set_show(self, show):
        self.show = show

    def set_seat_list(self, seat_list):
        self.seat_list = seat_list

    def set_payment_details(self, payment):
        self.payment = payment

    def set_total_bill(self):
        total_price = 0
        for seat in self.seat_list:
            total_price += seat.get_seat_type().value

        self.total_price = total_price

    def get_total_price(self):
        return self.total_price
