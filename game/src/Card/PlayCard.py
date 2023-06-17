from __future__ import annotations
from typing import TYPE_CHECKING


from game.src.Move import Move


if TYPE_CHECKING:
    from game.src.Card.Card import Card
    from game.src.Player import Player
    from game.src.Board.Board import Board
    from game.src.Game import Game


class PlayCard(Move):
    def __init__(self, card: Card) -> None:
        self.card = card
        super().__init__()

    def play(self, game: Game) -> None:
        self.card.play(game)
