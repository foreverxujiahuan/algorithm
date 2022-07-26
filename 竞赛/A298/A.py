def greatestLetter(s: str) -> str:
    s1 = "qwertyuiopasdfghjklzxcvbnm"
    s2 = s1.upper()
    res = ""
    d1 = dict()
    d2 = dict()
    for i in range(len(s1)):
        d1[s1[i]] = s2[i]
        d2[s2[i]] = s1[i]
    length = len(s)
    for i in range(length):
        c = s[i]
        if c in s1 and d1[c] in s:
            if d1[c] > res:
                res = d1[c]
        if c in s2 and d2[c] in s:
            if c > res:
                res = c
    return res


if __name__ == '__main__':
    s = "arRAzFif"
    res = greatestLetter(s)
    print(res)
