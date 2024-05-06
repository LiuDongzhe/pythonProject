from mahjong import mahjong
import random


class player:
    def __init__(self):
        self.hand = []
        self.preHand = []
        self.dropHand = []
        # self.dropHandIfBe

    def sortHand(self):
        tmp = []
        others = ['west', 'south', 'east', 'north', 'red', 'green', 'white']
        removeCards = []

        for card in self.hand:
            if card in others:
                tmp.append(card)
                removeCards.append(card)

        for card in removeCards:
            self.hand.remove(card)

        tmp.sort()
        self.hand.sort(reverse=True)
        for card in self.hand:
            tmp.append(card)
        self.hand = tmp

    def getHand(self):
        if self.preHand is not None:
            self.hand.append(self.preHand)

    def getPreHand(self, card):
        self.preHand = card

    def dropCard(self, card):
        if self.hand.index(card) and self.preHand == card:
            self.preHand = None
        elif self.hand.index(card):
            self.hand.remove(card)
        elif self.preHand == card:
            self.preHand = None


class AI:
    def __init__(self):
        self.hand = []
        self.preHand = None
        self.dropHand = None

    def AIsortHand(self):
        tmp = []
        others = ['west', 'south', 'east', 'north', 'red', 'green', 'white']
        removeAICards = []

        for card in self.hand:
            if card in others:
                tmp.append(card)
                removeAICards.append(card)

        for card in removeAICards:
            self.hand.remove(card)

        tmp.sort()
        self.hand.sort(reverse=True)
        for card in self.hand:
            tmp.append(card)
        self.hand = tmp

    def getHand(self):
        if self.preHand is not None:
            self.hand.append(self.preHand)

    def getPreHand(self, card):
        self.preHand = card

    # def dropCard(self, card):
    #     if self.hand.index(card) and self.preHand == card:
    #         self.preHand = None
    #     elif self.hand.index(card):
    #         self.hand.remove(card)
    #     elif self.preHand == card:
    #         self.preHand = None

    def dropCard(self):
        tmp = self.hand
        tmp.append(self.preHand)
        t = random.choice(tmp)
        tmp.remove(t)
        self.hand = tmp

        return t


if __name__ == '__main__':
    p = player()
    a = AI()
    m = mahjong()
    p.hand = ['bamboo1', 'south', 'east', 'bamboo2', 'bamboo7', 'wan2', 'wan4', 'circle1', 'circle7', 'white', 'red',
              'east']
    a.AIhand = ['bamboo3', 'south', 'east', 'bamboo2', 'bamboo7', 'wan2', 'wan4', 'circle1', 'circle7', 'white', 'red',
                'east']
    a.AIsortHand()
    p.sortHand()
    print(p.hand)
