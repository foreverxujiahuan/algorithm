from typing import List


def reverseString(s: List[str]) -> None:
    length = len(s)
    mid = length // 2
    for i in range(mid):
        j = length - i - 1
        s[i], s[j] = s[j], s[i]
    print(s)

s = list("hs")
reverseString(s)
