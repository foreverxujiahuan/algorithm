

# 告诉你一共有几个头和几只脚，让你求出鸡和兔各有几只

"""
1# x + y = 10
2# 2x + 4y = 28
2# - 2*1#
"""


def f(head, leg):
    for i in range(1, head+1):
        for j in range(1, head+1):
            if 2 * i + 4 * j == leg and i + j == head:
                return i, j
    return None, None


if __name__ == '__main__':
    h, l = 10, 28
    a, b = f(h, l)
    print(a, b)