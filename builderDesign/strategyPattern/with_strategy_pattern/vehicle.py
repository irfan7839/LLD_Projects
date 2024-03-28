from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, drive_obj):
        self.driveObject = drive_obj
    @abstractmethod
    def drive(self):
        self.driveObject.drive()
