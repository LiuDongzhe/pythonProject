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

def loadAIImage(card):
    AIimageLst = []

    if isinstance(card, list):
        for subCard in card:
            AIimageLst.append(pg.image.load(f'image/96/fulltiles/{subCard}.png').convert_alpha())
    else:
        AIimageLst.append(pg.image.load(f'image/96/fulltiles/{card}.png').convert_alpha())

    return AIimageLst

def loadRect(imageLst):
    rectLst = []

    i = 85 * (len(imageLst) - 1)
    if isinstance(imageLst, list):
        for _ in imageLst:
            rectLst.append(pg.Rect(i, 450, 96, 133))
            i -= 85
    else:
        rectLst.append(pg.Rect(1200, 450, 96, 133))
        # rectLst.append(pg.Rect(0, 0, 96, 133))
    return rectLst
def loadAIRect(AIimageLst):
    rectAILst = []

    i = 85 * (len(AIimageLst) - 1)
    if isinstance(AIimageLst, list):
        for _ in AIimageLst:
            rectAILst.append(pg.Rect(i, 450, 40, 133))
            i -= 85
    else:
        rectAILst.append(pg.Rect(1200, 450, 40, 133))
        # rectLst.append(pg.Rect(0, 0, 96, 133))
    return rectAILst
def handShow(screen, imageLst,rectLst):
    # i = 85 * (len(imageLst) - 1)
    for subImage, subRect in zip(imageLst, rectLst):
        screen.blit(subImage, subRect)
        # screen.blit(subImage, (i, 650))
        # i -= 85

def AIHandShow(screen, AIimageLst, rectAILst):
    for subImage, subRect in zip(AIimageLst, rectAILst):
        screen.blit(subImage, subRect)
def preHandShow(screen, image, rect):
    screen.blit(image, rect)
    # screen.blit(image, (1200, 650))


def clickHand(hand, rectLst):
    mousePos = pg.mouse.get_pos()

    for subRect in rectLst:
        if subRect.collidepoint(mousePos):
            subRect.y -= 20
            print(f'{hand[rectLst.index(subRect)]} clicked!')
        else:
            subRect.y = 650


def clickPreHand(preHand, rect):
    mousePos = pg.mouse.get_pos()

    if rect.collidepoint(mousePos):
        rect.y -= 20
        print(f'{preHand} clicked!')
    else:
        rect.y = 650