

"""
f(1) = 1
f(2) = 1
f(n) = f(n-1) + f(n-2)
f(3) = 2
f(4) = 3
f(5) = 5
f(6) = 8
f(7) = 13
"""


# 求出第n项fib数列的值f(n)
def f(n):
    if n == 1 or n == 2:
        return 1
    return f(n-1) + f(n-2)  # f(6) + f(5)


if __name__ == '__main__':
    n = 7
    ans = f(n)
    print(ans)
