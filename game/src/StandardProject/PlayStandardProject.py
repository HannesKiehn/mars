from __future__ import annotations
from typing import TYPE_CHECKING
from game.src.Move import Move


if TYPE_CHECKING:
    from game.src.Player import Player


class PlayStandardProject(Move):
    def __init__(self) -> None:
        super().__init__()

    def play(player: Player) -> None:
        return super().play()
