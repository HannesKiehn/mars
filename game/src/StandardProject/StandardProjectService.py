from __future__ import annotations
from ast import List
from typing import TYPE_CHECKING


from game.src.PriceService import PriceService
from game.src.StandardProject.PlayCity import PlayCity
from game.src.StandardProject.PlayGreenery import PlayGreenery

if TYPE_CHECKING:
    from game.src.Game import Game
    from game.src.Move import Move


class StandardProjectService:
    def __init__(self) -> None:
        pass

    def getPlayableStandardProjects(game: Game) -> List[Move]:
        return StandardProjectService.getPlayableCities(
            game
        ) + StandardProjectService.getPlayableGreeneries(game)

    def getPlayableCities(game: Game) -> List[PlayCity]:
        player = game.playerOnTurn
        if player.cash < PriceService.calculateCityPrice(player):
            return []
        else:
            return [PlayCity(0, 0)]

    def getPlayableGreeneries(game: Game) -> List[PlayGreenery]:
        player = game.playerOnTurn
        if player.cash < PriceService.calculateGreeneryPrice(player):
            return []
        else:
            return [PlayGreenery(0, 0)]
