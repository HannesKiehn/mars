from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game.src.Cards.Card import Card
    from game.src.Player import Player


class PriceService:
    def __init__(self) -> None:
        pass

    def calculatePrice(card: Card, player: Player) -> int:
        return card.basePrice
