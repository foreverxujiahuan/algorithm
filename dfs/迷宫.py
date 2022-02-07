def find_begin(a):
    for i in range(10):
        for j in range(10):
            if a[i][j] == '%':
                return i, j


def all_search(a, x, y,d):
    if x == 0 or x == 9 or y == 0 or y == 9:
        a[x][y] = '#'
        return True
    # 向上
    if (d != 8) and (a[x - 1][y] == 0):
        if all_search(a, x - 1, y, 2):
            a[x][y] = '#'
            return True
    # 向下
    if (d != 2) and (a[x + 1][y] == 0):
        if all_search(a, x + 1, y,8):
            a[x][y] = '#'
            return True
    # 向左
    if (d != 4) and (a[x][y - 1] == 0):
        if all_search(a, x, y - 1,6):
            a[x][y] = '#'
            return True
    # 向右
    if (d != 6) and (a[x][y + 1] == 0):
        if all_search(a, x, y + 1,4):
            a[x][y] = '#'
            return True


a = [[1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
     [1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
     [1, 0, 0, 0, 1, 0, 0, 1, 0, 1],
     [1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
     [1, 0, 1, 0, 0, 0, 0, 0, 1, 1],
     [1, 0, 1, 1, 0, 1, 0, 1, 1, 1],
     [1, 1, 1, 1, 0, 1, 0, 0, 0, 1],
     [1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
     [1, 0, '%', 0, 0, 1, 0, 0, 0, 1],
     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
x, y = find_begin(a)
d = 0
all_search(a, x, y,d)
for z in range(10):
    print(a[z])
