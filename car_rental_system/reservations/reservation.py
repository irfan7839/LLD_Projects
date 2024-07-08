import datetime

from car_rental_system.constants.reservation_status import ReservationStatus


class Reservation:
    def __init__(self):
        self.user = None
        self.vehicle = None
        self.id = 12312
        self.date = None
        self.start_time = None
        self.end_time = None
        self.reservation_status = None

    def create_reservation(self, user, vehicle, hours):
        self.date = datetime.datetime.today()
        self.start_time = datetime.datetime.now()
        self.end_time = self.start_time + datetime.timedelta(hours=hours)
        self.user = user
        self.vehicle = vehicle
        self.reservation_status = ReservationStatus.SCHEDULE
