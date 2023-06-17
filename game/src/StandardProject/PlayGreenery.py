from __future__ import annotations
from typing import TYPE_CHECKING
from game.src.Board.TileType import TileType

from game.src.Move import Move
from game.src.PriceService import PriceService

if TYPE_CHECKING:
    from game.src.Game import Game


class PlayGreenery(Move):
    def __init__(self, row: int, column: int) -> None:
        self.row = row
        self.column = column
        super().__init__("Greenery")

    def play(self, game: Game):
        player = game.playerOnTurn
        board = game.board
        player.cash -= PriceService.calculateGreeneryPrice(player)
        if not board.isOxygenMaxed():
            player.terraforming += 1
            board.oxygen += 1
        tile = board.getTile(self.row, self.column)
        tile.type = TileType.GREENERY
        tile.owner = player
