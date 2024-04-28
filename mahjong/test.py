import sys
import pygame as pg
from mahjong import mahjong


def loadImage(card):
    imageLst = []

    if isinstance(card, list):
        for subCard in card:
            imageLst.append(pg.image.load(f'image/96/fulltiles/{subCard}.png').convert_alpha())
    else:
        imageLst.append(pg.image.load(f'image/96/fulltiles/{card}.png').convert_alpha())

    return imageLst

def AIloadimage(card):
    AIimageLst = []
    if isinstance(card, list):
        for subCard in card:
            AIimage = pg.image.load(f'image/32/fulltiles/{subCard}.png').convert_alpha()
            rotated_AIimage = pg.transform.rotate(AIimage, 180)
            AIimageLst.append(rotated_AIimage)
    else:
        AIimage = pg.image.load(f'image/32/fulltiles/{card}.png').convert_alpha()
        rotated_AIimage = pg.transform.rotate(AIimage, 180)
        AIimageLst.append(rotated_AIimage)


    return AIimageLst

def loadImageDropDesk(card):
    imageLst = []

    if isinstance(card, list):
        for subCard in card:
            imageLst.append(pg.image.load(f'image/64/fulltiles/{subCard}.png').convert_alpha())
    else:
        imageLst.append(pg.image.load(f'image/64/fulltiles/{card}.png').convert_alpha())

    return imageLst


def loadRect(imageLst):
    rectLst = []

    i = 85 * (len(imageLst))
    if isinstance(imageLst, list):
        for _ in imageLst:
            rectLst.append(pg.Rect(i, 650, 86, 133))
            i -= 85
    else:
        rectLst.append(pg.Rect(1200, 650, 86, 133))

    return rectLst


def loadAIRect(AIimageLst):
    rectAILst = []
    i = 32 * (len(AIimageLst))
    if isinstance(AIimageLst,list):
        for _ in AIimageLst:
            rectAILst.append(pg.Rect(i,200,34,48))
            i -= 32
    else:
        rectAILst.append(pg.Rect(1200, 200,32,48))
    return rectAILst

def loadDroppedCard(imageLst):
    dropList = []

    i = 85 * (len(imageLst))
    if isinstance(imageLst, list):
        for _ in imageLst:
            dropList.append(pg.Rect(i, 450, 96, 133))
            i += 85
    else:
        dropList.append(pg.Rect(1285, 400, 96, 133))
        # rectLst.append(pg.Rect(0, 0, 96, 133))

    return dropList


def handShow(screen, imageLst, rectLst):
    # i = 85 * (len(imageLst) - 1)
    for subImage, subRect in zip(imageLst, rectLst):
        screen.blit(subImage, subRect)
        # screen.blit(subImage, (i, 650))
        # i -= 85


def AddPreHandToHand(preHand,hand):
    if preHand == list():
        pass
    elif preHand != list() and (len(hand) - 1) % 3 == 1:
        hand.append(preHand)
        sortHand(hand)


def AIHandShow(screen, AIimageLst, rectAILst):
    for subImage, subRect in zip(AIimageLst, rectAILst):
        screen.blit(subImage, subRect)


def preHandShow(screen, image, rect):
    # screen.blit(image, rect)
    for subImage, subRect in zip(image, rect):
        screen.blit(subImage, subRect)
    # screen.blit(image, (1200, 650))


def dropHandShow(screen, imageLst, dropList):
    # i = 85 * (len(imageLst) - 1)
    for subImage, subDrop in zip(imageLst, dropList):
        screen.blit(subImage, subDrop)
        # screen.blit(subImage, (i, 650))
        # i -= 85


def clickHand(hand, imageLst, rectLst, dropHand: list):
    mousePos = pg.mouse.get_pos()

    n = len(rectLst) - 1
    while n >= 0:
        if rectLst[n].collidepoint(mousePos) and rectLst[n].y > 610:
            rectLst[n].y -= 20
            # print(f'{hand} clicked!')
        elif rectLst[n].y == 610:  # Add the position of double click to array of drop
            dropHand.append(hand[n])

            #print(int((1200 - dropHand[0].x) / 85))
            #hand.remove(hand[int((1200 - dropHand[0].x) / 85)-1])
            #hand.append()
            hand.pop(n)
            del rectLst[n]
            del imageLst[n]
            print(hand)
            print(len(rectLst))

        else:
            rectLst[n].y = 650
        n -= 1
        print(dropHand)
    return dropHand

# def clickPreHand(preHand, preImageLst, rect, preDropHand:list):
#     mousePos = pg.mouse.get_pos()
#     n = len(rect) - 1
#     while n >= 0:
#         if rect[n].collidepoint(mousePos) and rect[n].y > 610:
#             rect[n].y -= 20
#             print(f'{preHand} clicked!')
#         elif rect[n].y == 610:  ##Add the position of double click to array of drop
#             preDropHand.append(rect[n])
#             del rect[n]
#             del preImageLst[n]
#             #rect[n].y == -200
#
#         else:
#             rect[n].y = 650
#
#     return preDropHand
