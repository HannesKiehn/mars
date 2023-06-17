from typing import List
from game.src.Cards.Card import Card
from game.src.Cards.InvestmentLoan import InvestmentLoan


class DeckOfCards:
    def __init__(self) -> None:
        self.cards = [InvestmentLoan()]
        pass

    def drawCard(self) -> Card:
        return self.cards.pop()
