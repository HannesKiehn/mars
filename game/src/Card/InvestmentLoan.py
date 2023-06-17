from __future__ import annotations
from game.src.Card.SimpleCard import SimpleCard
from game.src.Player import Player
from game.src.Tag import Tag


class InvestmentLoan(SimpleCard):
    def __init__(self) -> None:
        super().__init__(3, [Tag.EARTH, Tag.EVENT])

    def play(self, player: Player) -> None:
        player.cash -= super().getPrice(player)
        player.cashProd -= 1
        player.cash += 10

    def isPlayable(self, player: Player) -> bool:
        return super().getPrice(player) <= player.cash
