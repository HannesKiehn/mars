import random
from typing import List
from game.src.Move import Move
from game.src.Phase import Phase
from game.src.Player import Player


class Game:
    def __init__(self, playerCount) -> None:
        self.playerCount = playerCount
        self.players: List[Player] = []
        self.phase = Phase.START
        for _ in range(playerCount):
            self.players.append(Player())

    def isTerraformed():
        return False

    def playRandomGame(self):
        while not self.isTerraformed:
            self.phase = Phase.DRAFT
            for player in self.players:
                player.playLegalMove()

            self.phase = Phase.PLAYCARDS
            for player in self.players:
                player.playLegalMove()
                player.playLegalMove()
