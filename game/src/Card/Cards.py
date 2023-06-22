from __future__ import annotations
from ast import List
from typing import TYPE_CHECKING, Callable

from game.src.PriceService import PriceService

from game.src.Tag import Tag
from game.src.Card.CardVariation import CardVariation

if TYPE_CHECKING:
    from game.src.Game import Game


# Stuff to model (TODO)
# global requirements
# card resources
# rebates
# actions
# "unplaying" of actions for performance reasons
class Cards:
    def __init__(self) -> None:
        pass

    @staticmethod
    def getAllCardIds():
        basegame = ["releaseOfInertGases"]
        coorporateEra = ["investmentLoan"]
        return basegame + coorporateEra

    @staticmethod
    def play(cardId: str, variation: CardVariation, game: Game):
        player = game.playerOnTurn
        tags = Cards.getTags(cardId)
        basePrice = Cards.getBasePrice(cardId)
        player.cash -= PriceService.calculateCardPrice(basePrice, tags, player)
        player.playTags(tags)
        player.cards.remove(cardId)
        match cardId:
            case "investmentLoan":
                player.cashProd -= 1
                player.cash += 10
            case "releaseOfInertGases":
                player.terraforming += 2
        pass

    @staticmethod
    def getTags(cardId: str):
        match cardId:
            case "investmentLoan":
                return [Tag.EARTH, Tag.EVENT]
            case "releaseOfInertGases":
                return [Tag.EVENT]

    @staticmethod
    def getBasePrice(cardId: str):
        match cardId:
            case "investmentLoan":
                return 3
            case "releaseOfInertGases":
                return 14

    @staticmethod
    def isPlayable(cardId: str, game: Game):
        player = game.playerOnTurn
        tags = Cards.getTags(cardId)
        basePrice = Cards.getBasePrice(cardId)
        if player.cash < PriceService.calculateCardPrice(basePrice, tags, player):
            return False
        return True

    @staticmethod
    def getPlayableVariations(cardId: str, game: Game) -> List[CardVariation]:
        match cardId:
            case "asteroid" | "bigAsteroid":
                return Cards.getAllPlayersVariation()
        return [CardVariation()]  # Default case for cards that have no variation

    @staticmethod
    def getAllPlayersVariation(game: Game):
        variations = [CardVariation() for _ in range(game.playerCount)]
        for index, variation in enumerate(variations):
            variation.affectedPlayer = index
        return variations
