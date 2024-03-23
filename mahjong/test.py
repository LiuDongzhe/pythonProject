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


def handShow(screen, imageLst):
    i = 85 * (len(imageLst) - 1)
    for subImage in imageLst:
        screen.blit(subImage, (i, 650))
        i -= 85


def preHandShow(screen, image):
    screen.blit(image, (1200, 650))
