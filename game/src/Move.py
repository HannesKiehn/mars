from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from game.src.Player import Player
    from game.src.Board.Board import Board
    from game.src.Game import Game


class Move(ABC):
    def __init__(self, name: str) -> None:
        self.name = name
        pass

    @abstractmethod
    def play(game: Game) -> None:
        pass
