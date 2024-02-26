import numpy as np
import matplotlib.pyplot as plt

class die:
    def __init__(self, numSides=6, probSides=None, numDie=1):
        if probSides is None:
            probSides = [1 / numSides for _ in range(numSides)]
        self.numSides = [i for i in range(1, numSides + 1)]
        self.probSides = probSides
        self.numDie = numDie
        self.result = []
        self.ans = []
        self.totalNum = None

    def printDie(self):
        # print(self.numSides)
        # print(self.probSides)
        # print(self.result)
        print(self.ans[-1])

    def throwDice(self, totalNum):
        self.totalNum = totalNum
        for i in range(self.numDie):
            self.result.append(list(np.random.choice(a=self.numSides, size=self.totalNum, replace=True, p=self.probSides)))

    def compare(self):
        tmp = np.array(self.result).T
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
        plt.show()


if __name__ == '__main__':
    die1 = die(numDie=3)
    die1.throwDice(10000)
    die1.compare()
    die1.printDie()
    die1.printGraph()

