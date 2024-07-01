#  递归
#  斐波那契数列
#  1,1,2,3,5,8,13,21,34,55
#  f(n) = f(n-1) + f(n-2) # 列出递归的数学表达式

def f(n):
    if n < 2:
        return 1  # 确定递归的出口
    # 需要返回第n项斐波那契数列第值，最小坐标为0
    return f(n-1) + f(n-2)  # n>=2


# ans_0 = f(0)
# ans_1 = f(1)
# ans_5 = f(5)
ans_9 = f(9)

ans_2 = f(2)  # f(2) = f(1) + f(0) = 1 + 1 = 2
# print(ans_2)
ans_3 = f(3)  # f(3) = f(2) + f(1) = f(1) + f(0) + 1 = 1 + 1 + 1 = 3
ans_5 = f(5)  # f(5) = f(4) + f(3) = f(3) + f(2) + f(2) + f(1) = 3 + 2 + 2 + 1 = 8
# print(ans_5)
print(ans_9)


while True:
    pass


