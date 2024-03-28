from abc import ABC, abstractmethod

from vehicle import Vehicle
from drive_strategy import SpecialDriveStrategy


class SportsVehicle(Vehicle):
    def __init__(self):
        super().__init__(SpecialDriveStrategy())

    def drive(self):
        self.driveObject.drive()
