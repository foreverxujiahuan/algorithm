def isAnagram(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)

s = 'anagram'
t = 'nagaram'
res = isAnagram(s, t)
print(res)