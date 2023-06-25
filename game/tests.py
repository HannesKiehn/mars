from django.test import TestCase
from django import setup

import os

from game.src.Card.BasePrice import BasePrice


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mars.settings")
setup()


class CardPriceTestCase(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def testPlayerCanPlayInvestmentLoan(self):
        from game.src.Player import Player
        from game.src.Game import Game
        from game.src.Board.BoardType import BoardType
        from game.src.Card.PlayCard import PlayCard

        game = Game(2, BoardType.THARSIS)
        player = game.playerOnTurn
        player.cash = 3
        player.cards = ["investmentLoan"]
        moves = player.getLegalMoves(game)
        playLoan = list(filter(lambda move: isinstance(move, PlayCard), moves))[0]
        self.assertEqual(len(moves), 2)
        player.play(playLoan, game)
        self.assertEqual(player.cash, 10)


class BoardTestCase(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def testTharsisBoard(self):
        from game.src.Board.Board import Board

        from game.src.Board.BoardType import BoardType

        board = Board(BoardType.THARSIS)
        emptyLand = 0
        emptyOceans = 0
        empty = 0
        bonusSteel = 0
        bonusPlants = 0
        bonusTitanium = 0
        bonusCards = 0
        for tile in board.grid:
            if tile.isEmpty():
                empty += 1
            if tile.isEmptyLand():
                emptyLand += 1
            if tile.isEmptyOcean():
                emptyOceans += 1
            bonusSteel += tile.bonusSteel
            bonusPlants += tile.bonusPlants
            bonusTitanium += tile.bonusTitanium
            bonusCards += tile.bonusCards
        self.assertEqual(empty, 61)
        self.assertEqual(emptyLand, 48)
        self.assertEqual(emptyOceans, 12)
        self.assertEqual(bonusSteel, 11)
        self.assertEqual(bonusPlants, 38)
        self.assertEqual(bonusTitanium, 4)
        self.assertEqual(bonusCards, 6)


class RandomGameTestCase(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def testPlayRandomGame(self):
        from game.src.Game import Game
        from game.src.Board.BoardType import BoardType

        game = Game(2, BoardType.THARSIS)
        game.playRandomGame()

        self.assertEqual(game.board.oxygen, 14)
        # self.assertEqual(game.board.getOceans(), 9)
        # self.assertEqual(game.board.temperature, 8)

        self.assertTrue(game.players[0].cash >= 0)
        self.assertTrue(game.players[1].cash >= 0)


class EvalutationTestCase(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def testPlayEvaluatedGame(self):
        from game.src.Game import Game
        from game.src.Board.BoardType import BoardType
        import time

        t0 = time.time()
        game = Game(2, BoardType.THARSIS)
        game.playEvaluatedGame()
        t1 = time.time()
        print("Test took {}".format(t1 - t0))


class CardDataTestCase(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def testNumberOfCards(self):
        # self.assertEqual(len(BasePrice.PRICES), 208)
        totalPrice = 0
        for price in BasePrice.PRICES.values():
            totalPrice += price
        self.assertEqual(totalPrice, 2501)
