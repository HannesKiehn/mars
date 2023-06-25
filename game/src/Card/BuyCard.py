from __future__ import annotations
from typing import TYPE_CHECKING
from game.src.Card.CardVariation import CardVariation
from game.src.Card.Cards import Cards


from game.src.Move import Move


if TYPE_CHECKING:
    from game.src.Game import Game


class BuyCard(Move):
    def __init__(self, cardId: str) -> None:
        self.cardId = cardId
        super().__init__(cardId)

    def play(self, game: Game) -> None:
        player = game.playerOnTurn
        player.cash -= 3
        player.cards.append(self.cardId)
