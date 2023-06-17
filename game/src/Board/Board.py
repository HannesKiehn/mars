from __future__ import annotations
from ast import List
from typing import TYPE_CHECKING
from game.src.Board.Tile import Tile
from game.src.Board.TileType import TileType
from game.src.Board.BoardType import BoardType


class Board:
    def __init__(self, type: BoardType) -> None:
        self.oxygen: int = 0
        self.temperature: int = -30
        self.grid: List[Tile] = []
        if type == BoardType.THARSIS:
            self.initTharsisBoard()
        else:
            raise NotImplemented
        pass

    def initTharsisBoard(self) -> None:
        self.initEmptyGrid()
        self.initTharisTileTypes()
        self.initTharsisBonus()

    def initTharisTileTypes(self) -> None:
        self.getTile(0, 1).type = TileType.EMPTY_OCEAN
        self.getTile(0, 3).type = TileType.EMPTY_OCEAN
        self.getTile(0, 4).type = TileType.EMPTY_OCEAN

        self.getTile(1, 5).type = TileType.EMPTY_OCEAN

        self.getTile(3, 7).type = TileType.EMPTY_OCEAN

        self.getTile(4, 2).type = TileType.RESERVED_FOR_SPECIAL
        self.getTile(4, 3).type = TileType.EMPTY_OCEAN
        self.getTile(4, 4).type = TileType.EMPTY_OCEAN
        self.getTile(4, 5).type = TileType.EMPTY_OCEAN

        self.getTile(5, 5).type = TileType.EMPTY_OCEAN
        self.getTile(5, 6).type = TileType.EMPTY_OCEAN
        self.getTile(5, 7).type = TileType.EMPTY_OCEAN

        self.getTile(8, 4).type = TileType.EMPTY_OCEAN

    def initTharsisBonus(self) -> None:
        self.getTile(0, 0).bonusSteel = 2
        self.getTile(0, 1).bonusSteel = 2
        self.getTile(0, 3).bonusCards = 1

        self.getTile(1, 1).bonusSteel = 1
        self.getTile(1, 5).bonusCards = 2

        self.getTile(2, 0).bonusCards = 1
        self.getTile(2, 6).bonusSteel = 1

        for column in range(8):
            self.getTile(3, column).bonusPlants = 1
        self.getTile(3, 0).bonusTitanium = 1
        self.getTile(3, 4).bonusPlants = 2
        self.getTile(3, 7).bonusPlants = 2

        for column in range(9):
            self.getTile(4, column).bonusPlants = 2

        for column in range(8):
            self.getTile(5, column).bonusPlants = 1
        self.getTile(5, 1).bonusPlants = 2

        self.getTile(6, 5).bonusPlants = 1

        self.getTile(7, 0).bonusSteel = 2
        self.getTile(7, 2).bonusCards = 1
        self.getTile(7, 3).bonusCards = 1
        self.getTile(7, 5).bonusTitanium = 1

        self.getTile(8, 0).bonusSteel = 1
        self.getTile(8, 1).bonusSteel = 2
        self.getTile(8, 4).bonusTitanium = 2

    def initEmptyGrid(self) -> None:
        totalTiles: int = 61
        for _ in range(totalTiles):
            self.grid.append(Tile())

    # Counted from zero
    def getTile(self, row: int, column: int) -> Tile:
        rowoffset = [0, 5, 11, 18, 26, 35, 43, 50, 56]
        index = rowoffset[row] + column
        return self.grid[index]

    def getOceans() -> int:
        pass
