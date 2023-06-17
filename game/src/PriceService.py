from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from game.src.Card.Card import Card
    from game.src.Player import Player


class PriceService:
    def __init__(self) -> None:
        pass

    def calculateCardPrice(card: Card, player: Player) -> int:
        return card.basePrice

    def calculateCityPrice(player: Player) -> int:
        return 25

    def calculateGreeneryPrice(player: Player) -> int:
        return 23

    def calculateOceanPrice(player: Player) -> int:
        return 18

    def calculateAsteroidPrice(player: Player) -> int:
        return 18

    def calculatePowerPlantPrice(player: Player) -> int:
        return 11
