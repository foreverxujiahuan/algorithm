
def findbegin(a):
    for i in range(10):
        for j in range(10):
            if a[i][j] == '%':
                return i, j

def dfs(a, x, y, path):
    if a[x][y] == 1:
        return False
    if x == 0 or x == 9 or y == 0 or y == 9:
        path.append((x, y))
        return True
    path.append((x, y))
    # 向下
    if x+1 < len(a) and dfs(a, x+1, y, []):
        return True
    # 向左
    if y-1 >= 0 and dfs(a, x, y-1, []):
        return True
    # 向右
    if y+1 <= len(a[0]) == 0 and dfs(a, x, y+1, []):
        return True
    # 向上
    if x-1 >= 0 == 0 and dfs(a, x-1, y, []):
        return True
    path.pop()
    a[x][y] = 1


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
path = []
x,y = findbegin(a)
dfs(a,x,y, path)
for i, j in path:
    a[i][j] = '#'
for z in range(10):
    print (a[z])
