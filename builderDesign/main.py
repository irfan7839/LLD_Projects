from abc import ABCMeta, abstractmethod


class IBuilder(metaclass=ABCMeta):
    """The Builder Interface"""

    @abstractmethod
    def set_wall_material(self, value):
        """Set wall material"""

    @abstractmethod
    def set_building_type(self, value):
        """Set wall material"""

    @abstractmethod
    def set_number_doors(self, value):
        """Set wall material"""

    @abstractmethod
    def set_number_windows(self, value):
        """Set wall material"""

    @abstractmethod
    def get_result(self):
        """Set wall material"""


class HouseBuilder(IBuilder):
    """The Builder Interface"""

    def __init__(self):
        self.house = House()

    def set_wall_material(self, value):
        """Set wall material"""
        self.house.wall_material = value
        return self

    def set_building_type(self, value):
        """Set building type"""
        self.house.building_type = value
        return self

    def set_number_doors(self, value):
        """Set number of doors"""
        self.house.doors = value
        return self

    def set_number_windows(self, value):
        """Set number of windows"""
        self.house.doors = value
        return self

    def get_result(self):
        """get result"""
        return self.house


class House:
    def __init__(self, wall_material="fiber", doors=0, window=0, building_type="Apartment"):
        self.wall_material = wall_material
        self.windows = window
        self.doors = doors
        self.building_type = building_type

    def __str__(self):
        return "this is a {0}, with wall material {1}, total windows {2} and door {3}.".format(self.building_type,
                                                                                               self.wall_material,
                                                                                               self.windows, self.doors)


class Apartment:
    @staticmethod
    def construct():
        return HouseBuilder() \
            .set_building_type("Apartment") \
            .set_wall_material('bricks') \
            .set_number_doors(5).set_number_windows(3).get_result()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    apatment = Apartment().construct()
    print(apatment)
    pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
