from __future__ import annotations
from typing import TYPE_CHECKING
from game.src.Board.Board import Board
from game.src.Card.Card import Card
from game.src.Tag import Tag

if TYPE_CHECKING:
    from game.src.Game import Game
    from game.src.Player import Player


class InvestmentLoan(Card):
    def __init__(self) -> None:
        super().__init__(3, [Tag.EARTH, Tag.EVENT])

    def play(self, game: Game) -> None:
        player = game.playerOnTurn
        player.cash -= super().getPrice(player)
        player.cashProd -= 1
        player.cash += 10

    def isPlayable(self, player: Player) -> bool:
        return super().getPrice(player) <= player.cash
