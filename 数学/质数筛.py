def f(n):
    primes = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * 2, n + 1, p):
                primes[i] = False
        p += 1
    primes = [e for e in range(2, n) if primes[e]]
    return set(primes)



def eratosthenes_sieve(n):
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False  # 0 和 1 不是质数

    p = 2
    while p * p <= n:
        if prime[p]:
            # 将 p 的所有倍数标记为 False
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    # 返回所有质数
    return [p for p in range(n + 1) if prime[p]]


if __name__ == '__main__':
    # print(f(100))
    print(eratosthenes_sieve(25))