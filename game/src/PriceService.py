from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from game.src.Card.Card import Card
    from game.src.Player import Player
    from game.src.StandardProject.StandardProject import StandardProject


class PriceService:
    def __init__(self) -> None:
        pass

    def calculateCardPrice(card: Card, player: Player) -> int:
        return card.basePrice

    def calculateStandardProjectPrice(project: StandardProject, player: Player) -> int:
        return project.basePrice
