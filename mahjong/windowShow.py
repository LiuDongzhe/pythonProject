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


def loadImageDropDesk(dropHand):
    dropImageLst = []
    if isinstance(dropHand, list):
        for subCard in dropHand:
            dropImageLst.append(pg.image.load(f'image/32/fulltiles/{subCard}.png').convert_alpha())
    else:
        dropImageLst.append(pg.image.load(f'image/32/fulltiles/{card}.png').convert_alpha())

    return dropImageLst


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

def loadRectDropDesk(dropImageLst):
    dropRectLst = []
    y = len(dropImageLst) % 14
    for n in range(len(dropImageLst),0,-1):
        x = (n / 14 + 1)
        if n % 14 == 0:
            y = 14
        else:
            y -= 1
        dropRectLst.append(pg.Rect( 200 + y*32, 200 + x*42, 86, 133))
    return dropRectLst

def loadAIRect(AIimageLst):
    rectAILst = []
    i = 32 * (len(AIimageLst))
    if isinstance(AIimageLst, list):
        for _ in AIimageLst:
            rectAILst.append(pg.Rect(i, 200, 34, 48))
            i -= 32
    else:
        rectAILst.append(pg.Rect(1200, 200, 32, 48))
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


def AddPreHandToHand(preHand, hand):
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


def clickHand(hand, prehand, handImageLst, preImageLst, handRectLst, preRectLst):
    mousePos = pg.mouse.get_pos()

    n = len(handRectLst) + 1
    while n >= 0:
        if n == len(handRectLst) + 1:
            if preRectLst.collidepoint(mousePos) and preRectLst.y > 610:
                preRectLst.y -= 20
            elif preRectLst.y == 610:  # Add the position of double click to array of drop
                dropHand.append(prehand)
                prehand.pop(0)
                del preRectLst
                del preImageLst
                print(prehand)
            else:
                preRectLst.y = 650
        else:
            if handRectLst[n].collidepoint(mousePos) and handRectLst[n].y > 610:
                handRectLst[n].y -= 20
                # print(f'{hand} clicked!')
            elif handRectLst[n].y == 610:  # Add the position of double click to array of drop
                dropHand.append(hand[n])
                hand.pop(n)
                del handRectLst[n]
                del handImageLst[n]
                print(hand)
                print(len(handRectLst))

            else:
                handRectLst[n].y = 650
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

def interface():
    pg.init()
    size = width, height = 1600, 900
    screen = pg.display.set_mode(size)
    pg.display.set_caption('interface')

    interface = pg.image.load('interface/start.png')
    interface = pg.transform.smoothscale(interface, (160, 160))

    # ==
    background = pg.image.load('interface/interface.png')
    background = pg.transform.smoothscale(background, (1600, 900))

    Check_interface = 1

    while Check_interface == 1:
        screen.blit(background, (0, 0))
        screen.blit(interface, (770, 700))
        # screen.fill(background, (0, 0))
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
