import random

size = 8
blocks = [[0 for j in range(size)] for i in range(size)]

for i in range(size):
    for j in range(size):
        blocks[i][j] = random.choice([0, 1, 2])

for t in blocks:
    print(t)

print("-"*100)


def destroy(x, y, lists):
    dfs(x, y, lists, lists[x][y])
    for temp in lists:
        print(temp)


def dfs(x, y, lists, target):
    lists[x][y] = '#'
    # 向右
    if 0 <= x < len(lists) and 0 <= y + 1 < len(lists[0]) and lists[x][y+1] == target:
        dfs(x, y+1, lists, target)
    # 向上
    if 0 <= x-1 < len(lists) and 0 <= y < len(lists[0]) and lists[x-1][y] == target:
        dfs(x-1, y, lists, target)
    # 向左
    if 0 <= x < len(lists) and 0 <= y - 1 < len(lists[0]) and lists[x][y-1] == target:
        dfs(x, y-1, lists, target)
    # 向下
    if 0 <= x + 1 < len(lists) and 0 <= y < len(lists[0]) and lists[x+1][y] == target:
        dfs(x+1, y, lists, target)


destroy(2, 3, lists=blocks)


