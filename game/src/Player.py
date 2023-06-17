from __future__ import annotations
import random
from typing import TYPE_CHECKING, List
from game.src.PlayCard import PlayCard

if TYPE_CHECKING:
    from game.src.Cards.Card import Card
    from game.src.DeckOfCards import DeckOfCards
    from game.src.Move import Move


class Player:
    def __init__(self, cash) -> None:
        self.terraforming = 20
        self.cash = cash
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
        pass

    def drawCard(cards: DeckOfCards) -> Card:
        return cards.drawCard()

    def buyCard(self, card: Card) -> Card:
        if self.cash < 3:
            raise ValueError("Not enough cash to buy card")
        self.cash -= 3

    def play(self, move: Move) -> None:
        move.play(self)
        pass

    def getLegalMoves(self) -> List[Move]:
        return [PlayCard(self.cards[0])]

    def playLegalMove(self) -> None:
        legalMoves: List[Move] = self.getLegalMoves()
        move: Move = random.choice(legalMoves)
        self.play(move)
