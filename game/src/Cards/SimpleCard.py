from __future__ import annotations
from abc import ABC, abstractmethod
from ast import List
from game.src.Cards.Card import Card
from game.src.Player import Player
from game.src.Tag import Tag


class SimpleCard(Card):
    def __init__(self, basePrice: int, tags: List[Tag]) -> None:
        super().__init__(basePrice, tags)

    @abstractmethod
    def play(player: Player) -> None:
        raise NotImplementedError
