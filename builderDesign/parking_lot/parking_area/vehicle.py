
class Vehicle:
    def __init__(self):
        self.milage = 0
        self.name = ''
        self.capacity = 0
        self.number = ''
        self.manufacturer = ''

    def create_vehicle_details(self, milage, name, capacity, number, manufacturer):
        self.milage = milage
        self.name = name
        self.capacity = capacity
        self.number = number
        self.manufacturer = manufacturer
        print("vehicle created successfully")