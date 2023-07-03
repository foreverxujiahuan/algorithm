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


if __name__ == '__main__':
    print(f(100))