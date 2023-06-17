from __future__ import annotations
from typing import TYPE_CHECKING
from game.src.Board.TileType import TileType

if TYPE_CHECKING:
    from game.src.Player import Player


class Tile:
    def __init__(self) -> None:
        self.bonusPlants = 0
        self.bonusSteel = 0
        self.bonusTitanium = 0
        self.bonusCards = 0
        self.type = TileType.EMPTY_LAND
        self.owner: Player = None
        pass

    def isEmpty(self) -> bool:
        return (
            self.type == TileType.EMPTY_LAND
            or self.type == TileType.EMPTY_OCEAN
            or self.type == TileType.RESERVED_FOR_SPECIAL
        )

    def isEmptyLand(self) -> bool:
        return self.type == TileType.EMPTY_LAND

    def isEmptyOcean(self) -> bool:
        return self.type == TileType.EMPTY_OCEAN

    def isOcean(self) -> bool:
        return self.type == TileType.OCEAN

    def isOwned(self) -> bool:
        return self.owner is not None
