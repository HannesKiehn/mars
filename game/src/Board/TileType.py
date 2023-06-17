from enum import Enum, auto


class TileType(Enum):
    EMPTY_LAND = auto()
    EMPTY_OCEAN = auto()
    OCEAN = auto()
    GREENERY = auto()
    CITY = auto()
    RESERVED_FOR_SPECIAL = auto()
