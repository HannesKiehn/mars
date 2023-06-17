from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game.src.Player import Player


class Move(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def play(player: Player) -> None:
        pass
