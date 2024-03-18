from mahjong import mahjong


class player:
    def __init__(self):
        self.hand = []
        self.preHand = None
        self.dropHand = None

    def sortHand(self):
        pass

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
