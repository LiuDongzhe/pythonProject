from binaryTree import *
from player import *


def sortHand(hand):
    tmp = []
    others = ['west', 'south', 'east', 'north', 'red', 'green', 'white']
    removeCards = []

    for card in hand:
        if card in others:
            tmp.append(card)
            removeCards.append(card)

    for card in removeCards:
        hand.remove(card)

    tmp.sort()
    hand.sort(reverse=True)
    for card in hand:
        tmp.append(card)
    hand = tmp

    return hand


def winCheck(hand, lastCard):
    pairScore = 0
    hand.append(lastCard)
    hand = sortHand(hand)

    bTree = binaryTree(hand)

    for nod in bTree.treeLst[::-1]:
        if nod.num != 0:
            if nod.num == 2 and pairScore == 0:
                nod.num -= 2

            if nod == nod.parent.left and nod.parent == nod.parent.parent.left:
                while nod.num > 0 and nod.parent.num > 0 and nod.parent.parent.num > 0:
                    nod.num -= 1
                    nod.parent.num -= 1
                    nod.parent.parent.num -= 1

            if nod.num == 3:
                nod.num -= 3

    checkScore = 0
    for i in bTree.treeLst:
        checkScore += i.num

    if checkScore == 0:
        return True
    else:
        return False


def gangCheck():
    pass


def pengCheck():
    pass


if __name__ == '__main__':
    p = player()
    # p.hand = ['circle2', 'circle2', 'circle3', 'circle4', 'bamboo1', 'bamboo2', 'bamboo3', 'wan1', 'wan2', 'wan3']
    p.hand = ['a1', 'a1', 'a1', 'a2', 'a2', 'a2', 'w1', 'w2', 'w2', 'w2']

    print(winCheck(p.hand, 'w3'))
