def countWays(length) -> int:
    mod = 1e9 + 7
    ans = 2 ** length % mod
    return int(ans)


if __name__ == '__main__':
    length = 100000
    ans = countWays(length)
    print(ans)