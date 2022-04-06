def minBitFlips(start: int, goal: int) -> int:
    t1 = bin(start)[2:]
    t2 = bin(goal)[2:]
    if len(t1) < len(t2):
        t1 = '0' * (len(t2) - len(t1)) + t1
    if len(t2) < len(t1):
        t2 = '0' * (len(t1) - len(t2)) + t2
    cnt = 0
    for c1, c2 in zip(t1, t2):
        if c1 != c2:
            cnt += 1
    return cnt

res = minBitFlips(3, 4)
print(res)