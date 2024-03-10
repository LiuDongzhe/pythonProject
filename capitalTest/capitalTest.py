import numpy as np


class capitalTest:
    def __init__(self):
        with open('answer.txt', 'r') as f:
            readData = f.readlines()
        f.close()

        self.country = []
        self.capital = []

        for i in range(len(readData)):
            readData[i] = readData[i].replace('\n', '')
            readData[i] = readData[i].split(', ', 1)

            self.capital.append(readData[i][0])
            self.country.append(readData[i][1])

    def test(self, totalNum):
        score = 0
        for i in range(totalNum):
            num = np.random.choice(len(self.country), 4, replace=False)
            ansNum = np.random.choice(num, 1)
            titleCountry = self.country[int(ansNum)]
            ansCapital = self.capital[int(ansNum)]

            print(f'question {i + 1}:\n'
                  f'which is the capital of {titleCountry} ?')
            for k in range(len(num)):
                print(str(k + 1) + f'  {self.capital[num[k]]}')

            ans = int(input('choose correct one: '))

            if self.capital[num[ans]] == ansCapital:
                score += 1
            self.capital.remove(ansCapital)
            self.country.remove(titleCountry)

        print(f'total score: {score}')


if __name__ == '__main__':
    test = capitalTest()
    test.test(10)