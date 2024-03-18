from mahjong import mahjong


class player:
    def __init__(self):
        self.hand = []
        self.preHand = None
        self.dropHand = None

    def sortHand(self):
        """
        the order is:
        bamboo, circle, wan, west, south, east, north, red, green, white
        """
        tmp = []
        others = ['west', 'south', 'east', 'north', 'red', 'green', 'white']
        for card in self.hand:
            if card in others:
                tmp.append(card)
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


if __name__ == '__main__':
    p = player()
    m = mahjong()
    for i in range(13):
        p.getPreHand(m.drawCard())
        p.getHand()

    p.sortHand()
    print(p.hand)
