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
if p.preHand is not None:
    preImageLst = loadImage(p.preHand)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    handShow(screen, imageLst)
    if p.preHand is not None:
        preHandShow(screen, preImageLst[0])
    pg.display.update()
