import numpy as np
import matplotlib.pyplot as plt


class die:
    def __init__(self, numSides=6, probSides=None, numDie=1, fair=True):
        if probSides is None:
            probSides = [1 / numSides for _ in range(numSides)]
        self.numSides = [i for i in range(1, numSides + 1)]
        self.probSides = probSides
        self.numDie = numDie
        self.fair = fair
        self.result = []
        self.ans = []
        self.totalNum = None

    def printDie(self):
        # print(self.numSides)
        # print(self.probSides)
        print(self.result)
        print(self.ans[-1])

    def throwDice(self, totalNum):
        tmp = []
        self.totalNum = totalNum
        if self.fair:
            for i in range(self.numDie):
                self.result.append(list(np.random.choice(a=self.numSides, size=self.totalNum, replace=True, p=self.probSides)))
        else:
            for prob in self.probSides:
                tmp.append(list(np.random.choice(a=len(prob), size=self.totalNum, replace=True, p=prob)))
            self.result.append(tmp)

    def compare(self):
        tmp = np.array(self.result).T
        # print(tmp)
        isDiff = 0
        flag = 0
        for i in tmp:
            if len(np.unique(i)) == len(i):
                isDiff += 1
                flag += 1
                self.ans.append(isDiff / flag)
            else:
                flag += 1
                self.ans.append(isDiff / flag)

    def printGraph(self):
        x = [i for i in range(self.totalNum)]
        plt.plot(x, self.ans)
        # plt.ylim(0, 1.0)
        plt.xlabel('Frequency')
        plt.ylabel('Probability')
        plt.title(f'Total Probability: {self.ans[-1]}')
        plt.show()


if __name__ == '__main__':

    die1 = die(numDie=6)
    die1.throwDice(10000)
    die1.compare()
    # die1.printDie()
    die1.printGraph()
    # prob = [[1/6, 1/6, 1/6, 1/6, 1/6, 1/6],
    #         [1/8, 2/8, 1/8, 1/8, 2/8, 1/8],
    #         [1/8, 1/8, 1/8, 1/8, 1/8, 1/8, 1/8, 1/8]]
    # die2 = die(numDie=3, probSides=prob, fair=False)
    # die2.throwDice(5000)
    # die2.compare()
    # # die2.printDie()
    # die2.printGraph()
