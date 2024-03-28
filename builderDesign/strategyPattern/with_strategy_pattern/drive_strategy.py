from abc import ABC, abstractmethod


class DriveStrategy(ABC):
    @abstractmethod
    def drive(self):
        pass

    @abstractmethod
    def abcd(self):
        pass


class NormalDriveStrategy(DriveStrategy):

    def drive(self):
        print("Normal drive strategy")

    def abcd(self):
        print("abcd")


class SpecialDriveStrategy(DriveStrategy):

    def drive(self):
        print('sports drive strategy')

    def abcd(self):
        pass


if __name__ == '__main__':
    dr = SpecialDriveStrategy()
    dr.drive()
