from __future__ import annotations
import random
from typing import TYPE_CHECKING, List
from game.src.Card.Cards import Cards

from game.src.Card.PlayCard import PlayCard
from game.src.PassMove import PassMove
from game.src.StandardProject.PlayGreenery import PlayGreenery
from game.src.StandardProject.StandardProjectService import StandardProjectService
from game.src.Tag import Tag

if TYPE_CHECKING:
    from game.src.Card.Card import Card
    from game.src.Card.DeckOfCards import DeckOfCards
    from game.src.Move import Move
    from game.src.Game import Game
    from game.src.Board.Board import Board


class Player:
    def __init__(self, id) -> None:
        self.id = id
        self.corporation = None
        self.terraforming = 20
        self.cash = 0
        self.steel = 0
        self.titanium = 0
        self.plants = 0
        self.power = 0
        self.heat = 0
        self.cashProd = 0
        self.steelProd = 0
        self.titaniumProd = 0
        self.PlantsProd = 0
        self.powerProd = 0
        self.heatProd = 0
        self.cards = Cards.getAllCardIds()
        self.victoryPoints = 0
        self.tags = {
            Tag.BUILDING: 0,
            Tag.SPACE: 0,
            Tag.SCIENCE: 0,
            Tag.PLANT: 0,
            Tag.MICROBE: 0,
            Tag.ANIMAL: 0,
            Tag.POWER: 0,
            Tag.JOVIAN: 0,
            Tag.EARTH: 0,
            Tag.CITY: 0,
            Tag.EVENT: 0,
        }

        self.allowedToPlayInTurn = True
        pass

    def drawCard(cards: DeckOfCards) -> Card:
        return cards.drawCard()

    def buyCard(self, card: Card) -> Card:
        if self.cash < 3:
            raise ValueError("Not enough cash to buy card")
        self.cash -= 3

    def play(self, move: Move, game: Game) -> None:
        move.play(game)
        pass

    def getLegalMoves(self, game: Game) -> List[Move]:
        playableCards = self.getPlayableCards(game)
        passMove = PassMove()
        sp = StandardProjectService.getPlayableStandardProjects(game)
        return playableCards + [passMove] + sp

    def getPlayableCards(self, game: Game) -> List[PlayCard]:
        playCardList = []
        playableCards: List[str] = list(
            filter(lambda cardId: Cards.isPlayable(cardId, game), self.cards)
        )
        for card in playableCards:
            variations = Cards.getPlayableVariations(card, game)
            playCardList += list(
                map(lambda variation: PlayCard(card, variation), variations)
            )
        return playCardList

    def playLegalMove(self, game: Game) -> None:
        legalMoves: List[Move] = self.getLegalMoves(game)
        move: Move = random.choice(legalMoves)
        move.play(game)

    def nextTurn(self) -> None:
        self.cash += self.cashProd + self.terraforming
        self.steel += self.steelProd
        self.titanium += self.titaniumProd
        self.plants += self.PlantsProd
        self.heat += self.heatProd
        self.heat += self.power
        self.power = self.powerProd
        self.allowedToPlayInTurn = True

    def playTag(self, tag: Tag) -> None:
        pass

    def playTags(self, tags: List[Tag]) -> None:
        pass
