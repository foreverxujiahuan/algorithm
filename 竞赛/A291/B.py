from typing import List


def minimumCardPickup(cards: List[int]) -> int:
    d = dict()
    for i in range(len(cards)):
        d.setdefault(cards[i], []).append(i)
    res = 999999999
    for k, v in d.items():
        length = len(v)
        v.sort()
        for i in range(length-1):
            if v[i+1] - v[i] < res:
                res = v[i+1] - v[i]
    if res == 999999999:
        return -1
    return res + 1

if __name__ == '__main__':
    cards = [1,0,5,3]
    res = minimumCardPickup(cards)
    print(res)
