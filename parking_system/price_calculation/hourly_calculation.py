import math


class HourBasis:
    @staticmethod
    def get_total_cost(time_in_minute, price):
        t_hour = math.ceil(time_in_minute/60)
        return t_hour * price
