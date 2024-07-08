from enum import Enum


class Direction(Enum):
    UP = 'UP'
    DOWN = 'DOWN'


class State(Enum):
    IDLE = 'IDLE'
    MOVING = 'MOVING'
