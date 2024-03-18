import pygame as pg
from mahjong import mahjong
from player import player
from test import func


m = mahjong()
p = player()
for i in range(5):
    p.getPreHand(m.drawCard())
    p.getHand()

# func(m.drawCard())