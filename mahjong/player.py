from mahjong import mahjong


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

# AI策略

import random

# 定义麻将牌
tiles = ['1万', '2万', '3万', '4万', '5万', '6万', '7万', '8万', '9万',
         '1筒', '2筒', '3筒', '4筒', '5筒', '6筒', '7筒', '8筒', '9筒',
         '1条', '2条', '3条', '4条', '5条', '6条', '7条', '8条', '9条',
         '东风', '南风', '西风', '北风', '红中', '发财', '白板']


# 定义简单的AI策略，随机选择出牌
def ai_play_hand():
    return random.choice(tiles)


# 主程序
if __name__ == '__main__':
    print("欢迎来到麻将游戏！")
    while True:
        print("\n玩家1的回合:")
        player_tile = input("请选择要打出的牌：")

        # AI回合
        print("\nAI的回合:")
        ai_tile = ai_play_hand()
        print("AI打出了：", ai_tile)
        # 判断胜负
        winner = random.choice(["玩家1", "AI"])
        print("\n{}获胜！".format(winner))
        play_again = input("\n是否要再玩一局？(y/n)")
        if play_again.lower() != 'y':
            break
    print("谢谢游玩麻将游戏！")
    print(a.AIhand)
