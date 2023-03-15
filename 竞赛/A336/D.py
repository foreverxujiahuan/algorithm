from collections import Counter

t = [1,2] * 2 + [2,3,4] * 3 + [5,6] * 2

ans = Counter(t)
print(ans)
