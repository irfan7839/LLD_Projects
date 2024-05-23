from elevator_system.floor.floor import Floor


class Building:
    def __init__(self, floors):
        self.no_of_floors = floors
        self.list_of_floors = []

    def add_floors(self):
        for i in range(self.no_of_floors+1):
            floor = Floor(i)
            if i == 0:
                floor.add_up_button()
            elif i == self.no_of_floors:
                floor.add_down_button()
            else:
                floor.add_down_button()
                floor.add_up_button()
            self.list_of_floors.append(floor)


