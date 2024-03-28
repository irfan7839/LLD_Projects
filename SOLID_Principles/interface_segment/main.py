from abc import ABC, abstractmethod


# class Vehicle(ABC):
#     @abstractmethod
#     def fly(self):
#         pass
#
#     @abstractmethod
#     def move(self):
#         pass
#
#
# class Car(Vehicle):
#     def fly(self):
#         print("car can't fly")
#
#     def move(self):
#         print("car can move")
#
#
# class AirCraft(Vehicle):
#     def fly(self):
#         print("car can't fly")
#
#     def move(self):
#         print("car can move")

class Movable(ABC):
    @abstractmethod
    def go(self):
        pass


class Flyable(Movable):
    @abstractmethod
    def fly(self):
        pass


class AirCraft(Flyable):
    def go(self):
        print("Aircraft can move")

    def fly(self):
        print("Aircraft can fly")


class Car(Movable):
    def go(self):
        print("car can move")


if __name__ == '__main__':
    car = Car()
    aircraft = AirCraft()
    car.go()
    aircraft.go()
    aircraft.fly()
    pass
