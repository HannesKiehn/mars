from django.test import TestCase
from django import setup

import os


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mars.settings")
setup()


class CardPriceTestCase(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def testPlayerCanPlayInvestmentLoan(self):
        from game.src.Card.InvestmentLoan import InvestmentLoan
        from game.src.Player import Player

        player = Player(3)
        player.cards = [InvestmentLoan()]
        moves = player.getLegalMoves()
        self.assertEqual(len(moves), 1)
        player.play(moves[0])
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
