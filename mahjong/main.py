import pygame as pg
from mahjong import mahjong
from player import player
from test import *


m = mahjong()
p = player()

for i in range(13):
    p.getPreHand(m.drawCard())
    p.getHand()

p.sortHand()
# print(p.hand)
pg.init()
screen = pg.display.set_mode((1600, 900))
screen.fill((0, 100, 0))
pg.display.set_caption('MahJong')

imageLst = loadImage(p.hand)
rectLst = loadRect(p.hand)
if p.preHand is not None:
    preImageLst = loadImage(p.preHand)
    preRectLst = loadRect(p.preHand)

while True:
    screen.fill((0, 100, 0))
    handShow(screen, imageLst, rectLst)
    if p.preHand is not None:
        preHandShow(screen, preImageLst[0], preRectLst[0])

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            clickHand(p.hand, rectLst)
            clickPreHand(p.preHand, preRectLst[0])

    pg.display.update()
    pg.display.flip()

# test
