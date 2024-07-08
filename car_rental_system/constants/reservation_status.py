from enum import Enum


class ReservationStatus(Enum):
    COMPLETED = 'COMPLETED'
    CLOSED = 'CLOSED'
    SCHEDULE = 'SCHEDULE'
