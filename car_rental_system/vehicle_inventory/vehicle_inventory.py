class VehicleInventory:
    def __init__(self):
        self.vehicle_list = []

    def set_vehicles(self, vehicles):
        self.vehicle_list = vehicles

    def get_vehicles(self):
        return self.vehicle_list
