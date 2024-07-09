from enum import Enum


class ItemType(Enum):
    COKE = 'COKE',
    PEPSI = 'PEPSI',
    SODA = 'SODA',
    JUICE = 'JUICE'


class Coin(Enum):
    PENNY = 1
    NICKEL = 5
    DIME = 10
    QUARTER = 25

