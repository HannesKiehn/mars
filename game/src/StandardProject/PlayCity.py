from __future__ import annotations
from typing import TYPE_CHECKING
from game.src.Board.TileType import TileType
from game.src.Move import Move
from game.src.PriceService import PriceService

if TYPE_CHECKING:
    from game.src.Game import Game


class PlayCity(Move):
    def __init__(self, row: int, column: int) -> None:
        self.row = row
        self.column = column
        super().__init__("City")

    def play(self, game: Game):
        player = game.playerOnTurn
        board = game.board
        player.cash -= PriceService.calculateCityPrice(player)
        player.cashProd += 1
        tile = board.getTile(self.row, self.column)
        tile.type = TileType.CITY
        tile.owner = player
