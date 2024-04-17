def winCheck(hand):
    # 胡牌检查
    if len(hand) % 3 != 2:
        return False

    # 统计每种牌的数量
    count = {}
    for tile in hand:
        if tile not in count:
            count[tile] = 1
        else:
            count[tile] += 1

    # 判断是否有顺子或刻子
    for tile, num in count.items():
        if num >= 2:
            # 如果有两张相同的牌，则可以组成刻子
            if num % 3 == 0:
                count[tile] -= 3
            else:
                # 如果只有一张相同的牌，则需要有其他牌与之组成顺子
                for i in range(1, 8):
                    if (tile + i in count and count[tile + i] > 0) or (tile - i in count and count[tile - i] > 0):
                        count[tile] -= 1
                        if tile + i in count:
                            count[tile + i] -= 1
                        else:
                            count[tile - i] -= 1
                        break
        else:
                    return False

    # 判断是否还有剩余的单张牌
    for num in count.values():
        if num > 0:
            return False

    return True


def gangCheck(hand):
    # 杠牌检查
    if len(hand) % 3 != 0:
        return False

    # 统计每种牌的数量
    count = {}
    for tile in hand:
        if tile not in count:
            count[tile] = 1
        else:
            count[tile] += 1

    # 判断是否有四张相同的牌
    for num in count.values():
        if num == 4:
            return True

    return False


def pengCheck(hand):
    # 碰牌检查
    if len(hand) % 3 != 0:
        return False

    # 统计每种牌的数量
    count = {}
    for tile in hand:
        if tile not in count:
            count[tile] = 1
        else:
            count[tile] += 1

    # 判断是否有三张相同的牌
    for num in count.values():
        if num == 3:
            return True

    return False
