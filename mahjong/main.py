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

##From Cao
if p.dropHand is not None:
    dropImageLst = loadImage(p.dropHand)
    dropDropLst = loadRect(p.dropHand)


while True:
    screen.fill((0, 100, 0))  # The color of screen
    handShow(screen, imageLst, rectLst)
    if p.preHand is not None:
        preHandShow(screen, preImageLst, preRectLst)
    if p.dropHand is not None:
        drophandShow(screen, dropImageLst, p.dropHand)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            clickHand(p.hand, imageLst, rectLst, p.dropHand)
            clickHand(p.preHand, preImageLst, preRectLst, p.dropHand)#click prehand has bug


    pg.display.update()
    pg.display.flip()
