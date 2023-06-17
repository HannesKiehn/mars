from django.test import TestCase
from django import setup

import os


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mars.settings")
setup()


class CardPriceTestCase(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def testPlayerCanPlayInvestmentLoan(self):
        from game.src.Cards.InvestmentLoan import InvestmentLoan
        from game.src.Player import Player

        player = Player(3)
        player.cards = [InvestmentLoan()]
        moves = player.getLegalMoves()
        self.assertEqual(len(moves), 1)
        player.play(moves[0])
        self.assertEqual(player.cash, 10)
