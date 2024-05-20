from enum import Enum

from parking_system.price_calculation.fixed_charge import FixedBasis
from parking_system.price_calculation.hourly_calculation import HourBasis
from parking_system.price_calculation.minute_calculation import MinuteBasis


class PriceType(Enum):
    HOUR_TYPE = "ht"
    MINUTE_TYPE = "mt"
    FIXED_TYPE = "ft"


class PriceFactory:
    @staticmethod
    def get_price_strategy(strategy):
        if strategy == PriceType.HOUR_TYPE:
            return HourBasis()
        elif strategy == PriceType.MINUTE_TYPE:
            return MinuteBasis()
        elif strategy == PriceType.FIXED_TYPE:
            return FixedBasis()
        else:
            return None
