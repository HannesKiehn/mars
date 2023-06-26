from __future__ import annotations
from ast import List
import copy
from statistics import mean
import time
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from game.src.Game import Game
    from game.src.Move import Move
    from game.src.Player import Player


class Evalutation:
    def __init__(self) -> None:
        pass

    @staticmethod
    def getPointsForPlayer(player: Player) -> int:
        return player.terraforming

    @staticmethod
    def getPoints(playerId: int, game: Game) -> int:
        if game.playerCount == 1:
            return -game.turn  # Solo games favor less turns
        return Evalutation.getPointsForPlayer(game.getPlayer(playerId))

    @staticmethod
    def evaluateMove(move: Move, game: Game):
        playerId = game.playerOnTurn.id
        N = 10
        t0 = time.time()
        games: List[Game] = [copy.deepcopy(game) for _ in range(N)]
        t1 = time.time()
        print("Deep copy took {}".format(t1 - t0))
        for randomGame in games:
            move.play(randomGame)
            randomGame.playRandomGame()
        t2 = time.time()
        print("Playing the games took {}".format(t2 - t1))
        scores = list(
            map(lambda randomGame: Evalutation.getPoints(playerId, randomGame), games)
        )
        return mean(scores)

    def getBestMoveWithPrint(game: Game) -> Move:
        moves: List[Move] = game.playerOnTurn.getLegalMoves(game)
        print(
            "\nThere are {} legal moves for player {}".format(
                len(moves), game.playerOnTurn.id
            )
        )
        if len(moves) == 1:
            print(
                "Move {} is played, because it is the only move".format(moves[0].name)
            )
        scores = [Evalutation.evaluateMove(move, game) for move in moves]
        for index, move in enumerate(moves):
            print("Move {} has an average score of {}".format(move.name, scores[index]))
        return moves[scores.index(max(scores))]
