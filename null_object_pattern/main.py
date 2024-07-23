from LLD_Projects.null_object_pattern.vehicle_factory import VehicleFactory


class Main:
    @staticmethod
    def start():
        car = VehicleFactory().get_vehicle('CAR')
        bike = VehicleFactory().get_vehicle('BIKE')
        print(car.get_seats(), car.get_capacity())
        print(bike.get_capacity(), bike.get_seats())


main = Main()
main.start()
