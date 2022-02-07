from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    if not strs:
        return ''
    i = 0
    flag = 0
    res = ''
    while flag == 0:
        if i < len(strs[0]):
            c = strs[0][i]
        else:
            break
        for s in strs:
            if i < len(s) and s[i] != c:
                flag = 1
            if i >= len(s):
                flag = 1
        if flag == 0:
            res += c
        i += 1
    return res


strs = ["ab", "a"]
res = longestCommonPrefix(strs)
print(res)