
def isPowerOfThree(n: int) -> bool:
    while n >= 3:
        n = n/3
    return n == 1


n = 45
print(isPowerOfThree(n))
