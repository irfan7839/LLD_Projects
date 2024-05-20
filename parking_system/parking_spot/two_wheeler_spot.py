from parking_system.parking_spot.parking_spot import ParkingSpot


class TwoWheelerSpot(ParkingSpot):

    def assign_price(self):
        self.price = 20

