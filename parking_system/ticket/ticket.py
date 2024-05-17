import random
import string


class Ticket:
    def __init__(self):
        self.id = ''
        self.vehicle_number = ''
        self.vehicle_type = ''
        self.charges = 0
        self.parking_spot_id = None
        self.price_strategy = ''

    def generate_ticket(self, vehicle_no, v_type, spot, price_strategy):
        self.generate_ticket_id()
        self.vehicle_number = vehicle_no
        self.vehicle_type = v_type
        self.charges = spot.price
        self.parking_spot_id = spot.id
        self.price_strategy = price_strategy
        print(f'Your parking ticket for {v_type} of {vehicle_no} at {spot.id} entry time {spot.time}')

    def generate_ticket_id(self):
        length = 5
        characters = string.ascii_lowercase + string.digits
        random_id = ''.join(random.choice(characters) for _ in range(length))
        return random_id
