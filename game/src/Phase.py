from enum import Enum, auto


class Phase(Enum):
    START = auto()
    PRELUDE = auto()
    DRAFT = auto()
    PLAYCARDS = auto()
    FINALGREENERIES = auto()
    END = auto()
