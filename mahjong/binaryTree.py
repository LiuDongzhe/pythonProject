from player import *


class node:
    def __init__(self, val, num, left, right, parent):
        self.val = val
        self.num = num
        self.left = left
        self.right = right
        self.parent = parent

    def printNode(self, nodeName):
        print(nodeName.val)
        if nodeName.left is not None:
            print('left:')
            self.printNode(nodeName.left)
        if nodeName.right is not None:
            print('right:')
            self.printNode(nodeName.right)


noneNode = node(val='None', num=1, left=None, right=None, parent=None)


class binaryTree:
    def __init__(self, lst: list):
        self.root = None
        self.lst = lst[::-1]
        self.treeLst = []
        self.nameLst = []

        self.root = node(val=self.lst[0], num=1, left=noneNode, right=noneNode, parent=noneNode)
        self.lst.remove(self.lst[0])

        self.treeLst.append(self.root)
        self.nameLst.append(self.root.val)

        self.createTree()

    def createTree(self):
        if len(self.lst) == 0:
            # print('success')
            return True

        if self.lst[0] == self.treeLst[-1].val:
            # tmpNode = node(val=self.lst[0], right=None, left=None, parent=self.treeLst[-1].val)
            # self.treeLst[-1].right = tmpNode
            # self.treeLst.append(tmpNode)
            # self.lst.remove(self.lst[0])
            # self.nameLst.append(tmpNode.val)

            self.treeLst[-1].num += 1
            self.lst.remove(self.lst[0])

            self.createTree()

        elif self.lst[0][:-1] == self.treeLst[-1].val[:-1] and int(self.lst[0][-1]) - int(self.treeLst[-1].val[-1]) == 1:
            tmpNode = node(val=self.lst[0], num=1, right=noneNode, left=noneNode, parent=self.treeLst[-1])
            self.treeLst[-1].left = tmpNode
            self.treeLst.append(tmpNode)
            self.lst.remove(self.lst[0])
            self.nameLst.append(tmpNode.val)

            self.createTree()

        else:
            tmpNode = node(val=self.lst[0], num=1, right=noneNode, left=noneNode, parent=self.treeLst[-1])
            self.treeLst[-1].right = tmpNode
            self.treeLst.append(tmpNode)
            self.lst.remove(self.lst[0])
            self.nameLst.append(tmpNode.val)

            self.createTree()

    def printTree(self):
        print(self.nameLst)


if __name__ == '__main__':
    # hand = ['bamboo1', 'bamboo2', 'bamboo3', 'wan1', 'wan2', 'wan3', 'wan3', 'wan4', 'wan5', 'circle1', 'circle2',
    #         'circle3', 'white']
    p = player()

    p.hand = ['circle2', 'circle2', 'circle2', 'circle3', 'circle4', 'bamboo1', 'bamboo2', 'bamboo3', 'wan1', 'wan2', 'wan3']
    p.sortHand()

    bt = binaryTree(p.hand)
    # bt.createTree()

    bt.printTree()

    for i in bt.treeLst:
        if i.parent is not None:
            # print(f'val: {i.val}, num: {i.num} parent: {i.parent.val}')
            print(f'val: {i.val}, parent: {i.parent.val}, left: {i.left.val}')

    bt.root.printNode(bt.root)

    # a = 'bamboo1'
    # b = 'bamboo2'
    #
    # if a[:-1] == b[:-1]:
    #     print(1)
    # if int(b[-1]) - int(a[-1]) == 1:
    #     print(2)
