def hammingWeight(n: int) -> int:
    cnt = 0
    while n != 0:
        if n % 2 == 1:
            cnt += 1
        n = int(n/2)
    return cnt

n = 11
res = hammingWeight(11)
print(res)
