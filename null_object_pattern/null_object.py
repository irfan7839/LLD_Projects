from LLD_Projects.null_object_pattern.vehicle_abstract_class import VehicleAbstract


class NullObject(VehicleAbstract):

    def get_seats(self):
        return 0

    def get_capacity(self):
        return 0
