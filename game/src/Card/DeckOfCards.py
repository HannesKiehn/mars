from __future__ import annotations
from typing import TYPE_CHECKING, List
from game.src.Card.Card import Card
from game.src.Card.Cards import Cards

if TYPE_CHECKING:
    from game.src.StartingHand import StartingHand


class DeckOfCards:
    def __init__(self, startingHand: StartingHand) -> None:
        self.cards: List[str] = self.getShuffledDeck(startingHand)
        pass

    def getShuffledDeck(self, startingHand: StartingHand):
        cardIds = Cards.getAllCardIds()
        alreadyGone = []
        for cards in startingHand.cards.values():
            alreadyGone += cards
        return [card for card in cardIds if card not in alreadyGone]

    def drawCard(self) -> str:
        return self.cards.pop()
