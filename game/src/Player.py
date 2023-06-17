from __future__ import annotations
import random
from typing import TYPE_CHECKING, List

from game.src.Card.PlayCard import PlayCard
from game.src.PassMove import PassMove
from game.src.StandardProject.PlayGreenery import PlayGreenery

if TYPE_CHECKING:
    from game.src.Card.Card import Card
    from game.src.Card.DeckOfCards import DeckOfCards
    from game.src.Move import Move
    from game.src.Game import Game
    from game.src.Board.Board import Board


class Player:
    def __init__(self) -> None:
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
        self.cards = []

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

    def getLegalMoves(self) -> List[Move]:
        playableCards = self.getPlayableCards()
        passMove = PassMove()
        greeneries = [PlayGreenery(0, 0)]
        return playableCards + [passMove] + greeneries

    def getPlayableCards(self) -> List[PlayCard]:
        playableCards: List[Card] = list(
            filter(lambda card: card.isPlayable(self), self.cards)
        )
        return list(map(lambda card: PlayCard(card), playableCards))

    def playLegalMove(self, game: Game) -> None:
        legalMoves: List[Move] = self.getLegalMoves()
        move: Move = random.choice(legalMoves)
        move.play(game)

    def nextTurn(self) -> None:
        self.cash += self.cashProd
        self.steel += self.steelProd
        self.titanium += self.titaniumProd
        self.plants += self.PlantsProd
        self.heat += self.heatProd
        self.heat += self.power
        self.power = self.powerProd
        self.allowedToPlayInTurn = True
