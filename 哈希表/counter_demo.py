from collections import Counter

a = [1,2,3]
b = [2, 3,4,5,6]
c = [2]

ans = Counter()

count1 = Counter(a)
count2 = Counter(b)
count3 = Counter(c)

ans = ans + count1 + count2 + count3

d1 = dict()
d1.setdefault()

ans = sorted(ans.items(), key=lambda d: d[1], reverse=True)
print(ans)