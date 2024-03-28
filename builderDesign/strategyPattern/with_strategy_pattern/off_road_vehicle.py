from vehicle import Vehicle
from drive_strategy import SpecialDriveStrategy


class OffRoadVehicle(Vehicle):
    def __init__(self):
        super().__init__(SpecialDriveStrategy())

    def drive(self):
        self.driveObject.drive()
