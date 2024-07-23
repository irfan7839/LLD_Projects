from LLD_Projects.null_object_pattern.vehicle_abstract_class import VehicleAbstract


class Car(VehicleAbstract):

    def get_capacity(self):
        return 40

    def get_seats(self):
        return 5
