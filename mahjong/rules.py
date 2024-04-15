import random
tiles = [1, 2, 3, 4, 5, 6, 7, 8, 9] * 4
random.shuffle(tiles)
player_hand = []
for _ in range(13):

    player_hand.append(tiles.pop())
def winCheck(hand):
    if len(hand) == 14:
        return True
    else:
        return False
def gangCheck(hand, tile):
    if hand.count(tile) >= 4:
        return True
    else:
        return False


def pengCheck(hand, tile):
    if hand.count(tile) >= 2:
        return True
    else:
        return False
    while True:
        player_hand.append(tiles.pop())
        if winCheck(player_hand):
            print("Congratulations,you won!")
            break
        discard_tile = random.choice(player_hand)
        player_hand.remove(discard_tile)
        if gangCheck(player_hand, discard_tile):
            print("You can gang %d" % discard_tile)

        if pengCheck(player_hand, discard_tile):
            print("Yon can peng %d" % discard_tile)


