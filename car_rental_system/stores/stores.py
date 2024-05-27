from car_rental_system.constants.vehicle_status import VehicleStatus
from car_rental_system.reservations.reservation import Reservation


class Stores:
    def __init__(self, store_id, location):
        self.store_id = store_id
        self.location = location
        self.vehicle_inventory = None
        self.reservations = []

    def get_vehicles(self):
        return self.vehicle_inventory.get_vehicles()

    def set_vehicles(self, vehicles):
        self.vehicle_inventory = vehicles

    def reserve_vehicle(self, user, vehicle, hours):
        reserve_vehicle = Reservation()
        reserve_vehicle.create_reservation(user, vehicle, hours)
        self.reservations.append(reserve_vehicle)
        return reserve_vehicle

    def return_vehicle(self, reservation_id):
        self.reservations.remove()

    def pick_vehicle(self):
        for vehicle in self.vehicle_inventory:
            if vehicle.status == VehicleStatus.ACTIVE:
                self.vehicle_inventory.remove(vehicle)
                return vehicle
        return None
