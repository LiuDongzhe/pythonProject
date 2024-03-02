import matplotlib.pyplot as plt
import numpy as np
import random


class poker:
    def __init__(self):
        self.suits = [1, 2, 3, 4]
        self.cards = [i for i in range(1, 14)]
        # self.drawNum = drawNum
        self.deck = [(suit, card) for suit in self.suits for card in self.cards]
        self.totalNum = None
        self.res = []
        self.ans = []

    def printCards(self):
        # print(self.deck)
        print(self.res)
        print(self.ans)

    def shuffleCards(self):
        self.deck = [(suit, card) for suit in self.suits for card in self.cards]
        np.random.shuffle(self.deck)

    def drawCards(self, drawNum, totalNum):
        self.totalNum = totalNum
        tmp = []
        for i in range(totalNum):
            self.shuffleCards()
            for j in range(drawNum):
                card = self.deck[0]
                tmp.append(card)
                self.deck.remove(card)
            self.res.append(tmp)
            tmp = []

    def compare(self):
        tmp = []
        for i in range(self.totalNum):
            t = np.array(self.res[i]).T
            t = t[0]
            tmp.append(t)
        # print(tmp)
        isSame = 0
        flag = 0
        for i in range(self.totalNum):
            if np.all(tmp[i][0] == tmp[i]):
                flag += 1
                isSame += 1

                self.ans.append(isSame / flag)
            else:
                flag += 1
                self.ans.append(isSame / flag)

    def printGraph(self):
        x = [i for i in range(self.totalNum)]
        plt.plot(x, self.ans)
        plt.title(f'the probability is: {self.ans[-1]}')
        plt.xlabel('Frequency')
        plt.ylabel('Probability')
        # plt.ylim(0, 1.0)
        plt.show()


if __name__ == "__main__":
    poker1 = poker()
    poker1.shuffleCards()
    # poker1.printCards()
    poker1.drawCards(drawNum=5, totalNum=1000000)
    poker1.compare()
    # poker1.printCards()
    poker1.printGraph()
