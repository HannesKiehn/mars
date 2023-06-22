from __future__ import annotations
from typing import TYPE_CHECKING
from game.src.Card.CardVariation import CardVariation
from game.src.Card.Cards import Cards


from game.src.Move import Move


if TYPE_CHECKING:
    from game.src.Card.Card import Card
    from game.src.Player import Player
    from game.src.Board.Board import Board
    from game.src.Game import Game


class PlayCard(Move):
    def __init__(self, cardId: str, variation: CardVariation) -> None:
        self.cardId = cardId
        self.variation = variation
        super().__init__(cardId)

    def play(self, game: Game) -> None:
        Cards.play(self.cardId, self.variation, game)
