import datetime

from parking_system.parking_manager_factory.parking_manager_factory import PSMFactory
from parking_system.ticket.ticket import Ticket
from parking_system.vehicle.vehicle import Vehicle


class EntryGate:
    def __init__(self):
        self.parking_spot = None
        self.parking_space = None
        self.parking_time = datetime.datetime.now()
        self.vehicle = None

    def get_vehicle_spot(self, vehicle_type):
        self.parking_spot = PSMFactory.get_parking_manager(vehicle_type)
        self.parking_space = self.parking_spot.finding_parking_space()

    def park_vehicle(self, parking_spot):
        parking_spot.park_vehicle(self.vehicle)
        self.generate_ticket()

    def generate_ticket(self):

        v_no = self.vehicle.vehicle_number
        v_type = self.vehicle.v_type
        spot = self.parking_space.id
        Ticket.generate_ticket(vehicle_no=v_no, v_type=v_type, spot=spot.id)

    def get_vehicle_details(self, v_type, v_no):
        self.vehicle = Vehicle(v_type, v_no)
        return self.vehicle

