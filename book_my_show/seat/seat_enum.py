from enum import Enum


class SeatType(Enum):
    Platinum = 500,
    Gold = 400,
    Silver = 300


class SeatStatus(Enum):
    AVAILABLE = 'AVAILABLE',
    BOOKED = 'BOOKED',
    NOT_AVAILABLE = 'NOT_AVAILABLE'
