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

def loadImageDropDesk(card):
    imageLst = []

    if isinstance(card, list):
        for subCard in card:
            imageLst.append(pg.image.load(f'image/32/fulltiles/{subCard}.png').convert_alpha())
    else:
        imageLst.append(pg.image.load(f'image/32/fulltiles/{card}.png').convert_alpha())

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

def loadDroppedCard(imageLst):
    dropList = []

    i = 85 * (len(imageLst) )
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


def preHandShow(screen, image, rect):
    #screen.blit(image, rect)
    for subImage, subRect in zip(image, rect):
        screen.blit(subImage, subRect)
    # screen.blit(image, (1200, 650))

def drophandShow(screen, imageLst, dropList):
    # i = 85 * (len(imageLst) - 1)
    for subImage, subDrop in zip(imageLst, dropList):
        screen.blit(subImage, subDrop)
        # screen.blit(subImage, (i, 650))
        # i -= 85



def clickHand(hand, imageLst, rectLst, dropHand:list):

    mousePos = pg.mouse.get_pos()

    n = len(rectLst) - 1
    while n >= 0:
        if rectLst[n].collidepoint(mousePos) and rectLst[n].y > 610:
            rectLst[n].y -= 20
            print(f'{hand} clicked!')
        elif rectLst[n].y == 610:  ##Add the position of double click to array of drop
            dropHand.append(rectLst[n])
            print(dropHand)
            del rectLst[n]
            del imageLst[n]

        else:
            rectLst[n].y = 650
        n -= 1
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