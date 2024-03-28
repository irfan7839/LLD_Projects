from vehicle import Vehicle
from drive_strategy import NormalDriveStrategy


class GoodsVehicle(Vehicle):
    def __init__(self):
        super().__init__(NormalDriveStrategy())

    def drive(self):
        self.driveObject.drive()
