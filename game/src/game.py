import random
from typing import List
from game.src.Board.Board import Board
from game.src.Board.BoardType import BoardType
from game.src.Card.DeckOfCards import DeckOfCards
from game.src.Evalutation import Evalutation
from game.src.Move import Move
from game.src.Phase import Phase
from game.src.Player import Player
from game.src.StartingHand import StartingHand


class Game:
    def __init__(self, playerCount: int, boardType: BoardType) -> None:
        if playerCount < 1:
            raise ValueError("Playercount must be at least 1")
        self.playerCount = playerCount
        self.players: List[Player] = []
        self.phase = Phase.START
        self.board = Board(boardType)
        for id in range(playerCount):
            self.players.append(Player(id))
        self.playerOnTurn = self.players[0]
        self.deck = None
        self.turn = 0
        self.moves: List[Move] = []

    def getPlayer(self, playerId: int) -> Player:
        player = next(filter(lambda player: player.id == playerId, self.players), None)
        if player is None:
            raise ValueError("No player with this id")
        return player

    def isTerraformed(self):
        return self.board.isOxygenMaxed()

    def nextPlayer(self):
        index = self.players.index(self.playerOnTurn)
        self.playerOnTurn = self.players[(index + 1) % self.playerCount]

    def playRandomGame(self, startingHand=None):
        if startingHand is None:
            startingHand = StartingHand(self.playerCount)
        self.deck = DeckOfCards(startingHand)
        while not self.isTerraformed():
            while self.turnIsInProgress():
                if self.playerOnTurn.allowedToPlayInTurn:
                    self.playerOnTurn.playLegalMove(self)
            self.nextTurn()

    # for testing purposes
    def playEvaluatedGame(self, startingHand=None):
        self.players[0].startingHand = startingHand
        while not self.isTerraformed():
            while self.turnIsInProgress():
                if self.playerOnTurn.allowedToPlayInTurn:
                    bestMove = Evalutation.getBestMoveWithPrint(self)
                    bestMove.play(self)
                    self.moves.append(bestMove)
            self.nextTurn()

    def nextTurn(self) -> None:
        self.turn += 1
        for player in self.players:
            player.nextTurn()

    def turnIsInProgress(self) -> bool:
        playersAllowedToPlay = list(
            filter(lambda player: player.allowedToPlayInTurn, self.players)
        )
        return len(playersAllowedToPlay) > 0
