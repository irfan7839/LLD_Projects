class Vehicles:
    def __init__(self):
        self.vehicle_number = ''
        self.vehicle_type = ''
        self.milage = ''
        self.manufacturer = ''
        self.status = ''

    def set_vehicle_number(self, vehicle_no):
        self.vehicle_number = vehicle_no

    def set_vehicle_type(self, vehicle_type):
        self.vehicle_type = vehicle_type

    def set_vehicle_milage(self, vehicle_milage):
        self.milage = vehicle_milage

    def set_vehicle_manufacturer(self, manufacturer):
        self.manufacturer = manufacturer

    def set_vehicle_status(self, status):
        self.status = status

    def get_vehicle_number(self):
        return self.vehicle_number

    def get_vehicle_type(self):
        return self.vehicle_type

    def get_vehicle_milage(self):
        return self.milage

    def get_vehicle_manufacturer(self):
        return self.manufacturer

    def get_vehicle_status(self):
        return self.status
