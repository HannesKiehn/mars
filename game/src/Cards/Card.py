from __future__ import annotations
from abc import ABC, abstractmethod
from ast import List
from typing import TYPE_CHECKING

from game.src.Tag import Tag
from game.src.PriceService import PriceService

if TYPE_CHECKING:
    from game.src.Player import Player


class Card(ABC):
    def __init__(self, basePrice: int, tags: List[Tag]) -> None:
        self.basePrice = basePrice
        self.tags = tags
        pass

    @abstractmethod
    def isPlayable() -> bool:
        pass

    @abstractmethod
    def play(player: Player) -> None:
        pass

    def getPrice(self, player: Player) -> int:
        return PriceService.calculatePrice(self, player)
