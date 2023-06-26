import random
from game.src.Card.Cards import Cards
from game.src.Corporation.Corporations import Corporations


# Change to single player? We need random setup for other players
class StartingHand:
    CORPORATIONS_PER_PLAYER = 2
    CARDS_PER_PLAYER = 10

    def __init__(self, playerCount: int) -> None:
        self.playerCount = playerCount
        self.corporations = self.getCorporations()
        self.cards = self.getCards()
        pass

    def getCorporations(self):
        randomCorps = random.sample(
            Corporations.IDS, self.playerCount * self.CORPORATIONS_PER_PLAYER
        )
        corporations = self.emptyListDict()
        for i, corp in enumerate(randomCorps):
            corporations[i % self.playerCount] += [corp]
        return corporations

    def getCards(self):
        randomCards = random.sample(
            Cards.getAllCardIds(), self.playerCount * self.CARDS_PER_PLAYER
        )
        cards = self.emptyListDict()
        for i, card in enumerate(randomCards):
            cards[i % self.playerCount] += [card]
        return cards

    def emptyListDict(self):
        emptyDict = {}
        for i in range(self.playerCount):
            emptyDict[i] = []
        return emptyDict
