import random


class mahjong:
    def __init__(self):
        suits = ['circle', 'bamboo', 'wan']
        winds = ['north', 'west', 'south', 'east']
        others = ['red', 'white', 'green']
        cards = [i for i in range(1, 10)]
        self.deck = [f'{suit}{card}' for suit in suits for card in cards]
        self.deck += winds
        self.deck += others
        self.deck *= 4
        self.shuffleCards()

    def shuffleCards(self):
        random.shuffle(self.deck)

    def printMahJong(self):
        return self.deck

    def drawCard(self):
        card = self.deck[0]
        self.deck.remove(card)
        return card


if __name__ == '__main__':
    m = mahjong()
    print(len(m.printMahJong()))
    print(m.drawCard())
    print(len(m.printMahJong()))
