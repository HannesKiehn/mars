from game.src.Board.BoardType import BoardType
from game.src.Evalutation import Evalutation
from game.src.Game import Game
from game.src.PickCorporation import PickCorporation
from game.src.StartingHand import StartingHand


class GameEvaluation:
    def __init__(self) -> None:
        pass

    def evaluateStartingHandSinglePlayer(startingHand: StartingHand):
        corps = startingHand.corporations
        N = 10
        scores = {corps[0][0]: 0, corps[0][1]: 0}
        for _ in range(N):
            game = Game(1, BoardType.THARSIS)
            game.playEvaluatedGame(startingHand)
            turns = -Evalutation.getPoints(0, game)
            firstMove = game.moves[0]
            if not isinstance(firstMove, PickCorporation):
                raise ValueError("First move should be picking a corp")
            scores[firstMove.corporationId] += turns
        print(scores)
