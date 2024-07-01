
# n = 5
# i = 2
# 取余
# 5 % 2 = 1
# 6 % 2 = 0
# 7 % 3 = 1

# 10000

# 7 ,3.5 4,5,6

# 因数, 6, 2和3,

def is_prime(n: int) -> bool:
    for i in range(2, 1 + n//2):
        if n % i == 0:
            return False
    return True


def f(n):
    prime = [i for i in range(2, n+1) if is_prime(i)]
    ans = []
    for p in prime:
        while n % p == 0 and n > 1:
            ans.append(p)
            n = n // p
    return ans


if __name__ == '__main__':
    n = 12
    ans = f(n)
    print(ans)
