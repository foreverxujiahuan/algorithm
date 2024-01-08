def min_operations(x, y):
    operations = 0

    # 逐步缩小x和y之间的差距
    while x != y:
        # 如果x大于y，则选择通过除以11、除以5、减1中操作次数较少的方式逼近y
        if x > y:
            if x % 11 == 0:
                x //= 11
            elif x % 5 == 0:
                x //= 5
            else:
                x -= 1
        # 如果x小于y，则选择通过加1逼近y
        else:
            x += 1
        operations += 1

    return operations

# 示例
x = 54
y = 2
result = min_operations(x, y)
print(result)
