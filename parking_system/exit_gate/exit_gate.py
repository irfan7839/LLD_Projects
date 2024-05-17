import datetime

from parking_system.parking_manager_factory.parking_manager_factory import PSMFactory


class ExitGate:
    def __init__(self):
        self.exit_time = datetime.datetime.now()
        self.total_price = 0
        self.price_calculation_strategy = None
        self.spot = None

    def calculate_total_price(self, price_strategy):
        self.price_calculation_strategy = price_strategy
        pass

    def remove_vehicle(self, ticket):
        v_type = ticket.vehicle_type
        spot_id = ticket.parking_spot_id
        spots = PSMFactory.get_parking_manager(v_type)
        for spot in spots:
            if spot.id == spot_id:
                spot.remove_vehicle()
                break
        



