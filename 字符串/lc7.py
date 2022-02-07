import math


def reverse(x: int) -> int:
    if x < 0:
        if -int(str(x)[::-1].replace('-', '')) < math.pow(-2, 31):
            return 0
        return -int(str(x)[::-1].replace('-', ''))
    if int(str(x)[::-1]) > math.pow(2, 31)-1:
        return 0
    return int(str(x)[::-1])

x = -123
print(reverse(x))