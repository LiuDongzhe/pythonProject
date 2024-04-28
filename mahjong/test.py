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


def loadAIRect(AIimageLst):
    rectAILst = []


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
            dropHand.append(rectLst[n])

            #print(int((1200 - dropHand[0].x) / 85))
            hand.remove(hand[int((1200 - dropHand[0].x) / 85)-1])
            #hand.append()

            del rectLst[n]
            del imageLst[n]
            print(hand)
            print(len(rectLst))

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

def interface():

    pg.init()
    size = width, height = 1600, 900
    screen = pg.display.set_mode(size)
    pg.display.set_caption('interface')

    interface = pg.image.load('interface/start.png')
    interface = pg.transform.smoothscale(interface, (160, 160))

    #==
    background = pg.image.load('interface/interface.png')
    background = pg.transform.smoothscale(background, (1600, 900))

    Check_interface = 1

    while Check_interface == 1:
        screen.blit(background, (0, 0))
        screen.blit(interface, (770, 700))
        #screen.fill(background, (0, 0))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if 770 <= event.pos[0] <= 930 and 700 <= event.pos[1] <= 860:
                    Check_interface = 0

        pg.display.update()
        pg.display.flip()







def player_interface():
    pg.init()
    size = width, height = 1600, 900
    screen = pg.display.set_mode(size)
    pg.display.set_caption('player_interface')

    player_interface = pg.image.load('win/win.png')
    player_interface = pg.transform.smoothscale(player_interface, (1600, 900))

    Restart = pg.image.load('win/restart.png')
    Restart = pg.transform.smoothscale(Restart, (160, 160))

    Check_interface = 1

    while Check_interface == 1:
        screen.blit(player_interface, (0, 0))
        screen.blit(Restart, (730, 600))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if 740 <= event.pos[0] <= 900 and 600 <= event.pos[1] <= 760:
                    Check_interface = 0

        pg.display.update()
        pg.display.flip()

def computer_interface():
    pg.init()
    size = width, height = 1600, 900
    screen = pg.display.set_mode(size)
    pg.display.set_caption('player_interface')

    computer_interface = pg.image.load('win/winning_of_computer.png')
    computer_interface = pg.transform.smoothscale(computer_interface, (1600, 900))

    Restart = pg.image.load('win/restart.png')
    Restart = pg.transform.smoothscale(Restart, (160, 160))

    Check_interface = 1

    while Check_interface == 1:
        screen.blit(computer_interface, (0, 0))
        screen.blit(Restart, (730, 600))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if 740 <= event.pos[0] <= 900 and 600 <= event.pos[1] <= 760:
                    Check_interface = 0

        pg.display.update()
        pg.display.flip()
def restart():
    pg.init()
    size = width, height = 1600, 900

    screen = pg.display.set_mode(size)
    pg.display.set_caption('Restart')

    Restart = pg.image.load('win/restart.png')
    Restart = pg.transform.smoothscale(Restart, (60, 60))

    Check_interface = 1

    while Check_interface == 1:
        screen.blit(Restart, (30, 30))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if 30 <= event.pos[0] <= 90 and 30 <= event.pos[1] <= 90:
                    Check_interface = 0

        pg.display.update()
        pg.display.flip()

