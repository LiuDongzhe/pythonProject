import random
import matplotlib.pyplot as plt

def drawCards():
    suits = ['1', '2', '3', '4']
    cards = [str(i) for i in range(1, 14)]
    deck = [(suit, card) for suit in suits for card in cards]
    random.shuffle(deck)
    return deck


def prob(num):
    sameSuit = 0
    p = []
    i = 0
    while i < num:
        i += 1
        deck = drawCards()
        card1 = random.choice(deck)
        deck.remove(card1)
        card2 = random.choice(deck)
        if card1[0] == card2[0]:
            sameSuit += 1
        p.append(sameSuit / i)
    return p


def printGraph(p, num):
    x = [i for i in range(num)]
    plt.plot(x, p)
    plt.title(f'the probability is: {p[-1]}')
    plt.xlabel('Frequency')
    plt.ylabel('Probability')
    plt.show()


if __name__ == "__main__":
    num = 10000
    p = prob(num)
    printGraph(p, num)
