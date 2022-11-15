from collections import Counter


s1 = "你你好,这个多少钱"
s2 = "你好呀，我想问一下这个多少钱"

counter1, counter2 = Counter(s1), Counter(s2)
t1 = (counter1 & counter2).values()
t2 = (counter1 | counter2).values()
ans = sum(t1) / sum(t2)

print(ans)
