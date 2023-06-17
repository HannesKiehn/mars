from __future__ import annotations
from typing import TYPE_CHECKING

from game.src.Move import Move

if TYPE_CHECKING:
    from game.src.Game import Game


class PassMove(Move):
    def __init__(self) -> None:
        super().__init__("Pass")

    def play(self, game: Game) -> None:
        game.playerOnTurn.allowedToPlayInTurn = False
        game.nextPlayer()
        pass
