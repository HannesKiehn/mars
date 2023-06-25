from django.test import TestCase
from django import setup

import os

from game.src.Card.BasePrice import BasePrice
from game.src.Card.Tags import Tags
from game.src.Tag import Tag


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
        self.assertEqual(len(BasePrice.PRICES), 208)
        self.assertEqual(len(Tags.TAGS), 208)

    def testTotalPrice(self):
        totalPrice = 0
        for price in BasePrice.PRICES.values():
            totalPrice += price
        self.assertEqual(totalPrice, 2506)

    def testBuildingCards(self):
        buildingTags = 0
        totalPrice = 0
        for tagKey, tagValue in Tags.TAGS.items():
            if isinstance(tagValue, list):
                for i in tagValue:
                    if i == Tag.BUILDING:
                        buildingTags += 1
                        totalPrice += BasePrice.PRICES[tagKey]

        self.assertEqual(buildingTags, 67)
        self.assertEqual(totalPrice, 808)

    def testSpaceCards(self):
        spaceTags = 0
        totalPrice = 0
        for tagKey, tagValue in Tags.TAGS.items():
            if isinstance(tagValue, list):
                for i in tagValue:
                    if i == Tag.SPACE:
                        spaceTags += 1
                        totalPrice += BasePrice.PRICES[tagKey]

        self.assertEqual(spaceTags, 42)
        self.assertEqual(totalPrice, 852)

    def testScienceCards(self):
        scienceTags = 0
        totalPrice = 0
        for tagKey, tagValue in Tags.TAGS.items():
            if isinstance(tagValue, list):
                for i in tagValue:
                    if i == Tag.SCIENCE:
                        scienceTags += 1
                        totalPrice += BasePrice.PRICES[tagKey]
        totalPrice -= 11  # double counting of research
        self.assertEqual(scienceTags, 34)
        self.assertEqual(totalPrice, 339)

    def testPlantCards(self):
        plantTags = 0
        totalPrice = 0
        for tagKey, tagValue in Tags.TAGS.items():
            if isinstance(tagValue, list):
                for i in tagValue:
                    if i == Tag.PLANT:
                        plantTags += 1
                        totalPrice += BasePrice.PRICES[tagKey]

        self.assertEqual(plantTags, 21)
        self.assertEqual(totalPrice, 244)

    def testMicrobeCards(self):
        microbeTags = 0
        totalPrice = 0
        for tagKey, tagValue in Tags.TAGS.items():
            if isinstance(tagValue, list):
                for i in tagValue:
                    if i == Tag.MICROBE:
                        microbeTags += 1
                        totalPrice += BasePrice.PRICES[tagKey]

        self.assertEqual(microbeTags, 16)
        self.assertEqual(totalPrice, 139)

    def testAnimalCards(self):
        animalTags = 0
        totalPrice = 0
        for tagKey, tagValue in Tags.TAGS.items():
            if isinstance(tagValue, list):
                for i in tagValue:
                    if i == Tag.ANIMAL:
                        animalTags += 1
                        totalPrice += BasePrice.PRICES[tagKey]

        self.assertEqual(animalTags, 9)
        self.assertEqual(totalPrice, 97)

    def testPowerCards(self):
        plantTags = 0
        totalPrice = 0
        for tagKey, tagValue in Tags.TAGS.items():
            if isinstance(tagValue, list):
                for i in tagValue:
                    if i == Tag.POWER:
                        plantTags += 1
                        totalPrice += BasePrice.PRICES[tagKey]

        self.assertEqual(plantTags, 27)
        self.assertEqual(totalPrice, 275)

    def testJovianCards(self):
        plantTags = 0
        totalPrice = 0
        for tagKey, tagValue in Tags.TAGS.items():
            if isinstance(tagValue, list):
                for i in tagValue:
                    if i == Tag.JOVIAN:
                        plantTags += 1
                        totalPrice += BasePrice.PRICES[tagKey]

        self.assertEqual(plantTags, 12)
        self.assertEqual(totalPrice, 281)

    def testEarthCards(self):
        plantTags = 0
        totalPrice = 0
        for tagKey, tagValue in Tags.TAGS.items():
            if isinstance(tagValue, list):
                for i in tagValue:
                    if i == Tag.EARTH:
                        plantTags += 1
                        totalPrice += BasePrice.PRICES[tagKey]

        self.assertEqual(plantTags, 22)
        self.assertEqual(totalPrice, 272)

    def testCityCards(self):
        cityTags = 0
        totalPrice = 0
        for tagKey, tagValue in Tags.TAGS.items():
            if isinstance(tagValue, list):
                for i in tagValue:
                    if i == Tag.CITY:
                        cityTags += 1
                        totalPrice += BasePrice.PRICES[tagKey]

        self.assertEqual(cityTags, 12)
        self.assertEqual(totalPrice, 222)

    def testEventCards(self):
        eventTags = 0
        totalPrice = 0
        for tagKey, tagValue in Tags.TAGS.items():
            if isinstance(tagValue, list):
                for i in tagValue:
                    if i == Tag.EVENT:
                        eventTags += 1
                        totalPrice += BasePrice.PRICES[tagKey]

        self.assertEqual(eventTags, 37)
        self.assertEqual(totalPrice, 476)

    def testNoTagCards(self):
        notags = 0
        totalPrice = 0
        for tagKey, tagValue in Tags.TAGS.items():
            if isinstance(tagValue, list) and len(tagValue) == 0:
                totalPrice += BasePrice.PRICES[tagKey]
                notags += 1

        self.assertEqual(notags, 12)
        self.assertEqual(totalPrice, 87)
