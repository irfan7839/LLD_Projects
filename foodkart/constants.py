from enum import Enum


class OrderStatus(Enum):
    INITIATED = 'INITIATED',
    ACCEPTED = 'ACCEPTED',
    DELIVERED = 'DELIVERED'
