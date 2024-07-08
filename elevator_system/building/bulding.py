from elevator_system.floor.floor import Floor


class Building:
    def __init__(self, floors):
        self.no_of_floors = len(floors)
        self.list_of_floors = floors




