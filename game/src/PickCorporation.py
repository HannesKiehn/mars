from __future__ import annotations
from typing import TYPE_CHECKING
from game.src.Corporation.Corporations import Corporations

from game.src.Move import Move

if TYPE_CHECKING:
    from game.src.Game import Game


class PickCorporation(Move):
    def __init__(self, corporationId: str) -> None:
        self.corporationId = corporationId
        super().__init__("Pick " + str(corporationId))

    def play(self, game: Game) -> None:
        player = game.playerOnTurn
        Corporations.play(self.corporationId, player)
