
def firstUniqChar(s: str) -> int:
    if not s:
        return -1
    hash_map = dict()
    for t in s:
        if t in hash_map.keys():
            hash_map[t] += 1
        else:
            hash_map[t] = 1
    for i in range(len(s)):
        if hash_map[s[i]] == 1:
            return i
    return -1


s = "loveleetcode"
res = firstUniqChar(s)
print(res)
