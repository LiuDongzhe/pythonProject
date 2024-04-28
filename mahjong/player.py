from mahjong import mahjong


class player:
    def __init__(self):
        self.hand = []
        self.preHand = None
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
        self.AIHand = []
        self.AIpreHand = None
        self.AIdropHand = None

    def AIsortHand(self):
        AItmp = []
        AIothers = ['west', 'south', 'east', 'north', 'red', 'green', 'white']
        removeAICards = []

        for card in self.AIHand:
            if card in AIothers:
                AItmp.append(card)
                removeAICards.append(card)

        for card in removeAICards:
            self.AIHand.remove(card)

        AItmp.sort()
        self.AIHand.sort(reverse=True)
        for card in self.AIHand:
            AItmp.append(card)
        self.AIHand = AItmp

    def AIgetHand(self):
        if self.AIpreHand is not None:
            self.AIHand.append(self.AIpreHand)

    def AIgetPreHand(self, card):
        self.AIpreHand = card

    def AIdropCard(self, card):
        if self.AIHand.index(card) and self.AIpreHand == card:
            self.AIpreHand = None
        elif self.AIHand.index(card):
            self.AIHand.remove(card)
        elif self.AIpreHand == card:
            self.AIpreHand = None


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
    print(a.AIhand)
