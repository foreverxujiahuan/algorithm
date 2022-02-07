def climbStairs(n: int) -> int:
    pre = 0
    cur = 1
    for _ in range(n):
        pre, cur = cur, pre + cur
    return cur

res = climbStairs(4)
print(res)