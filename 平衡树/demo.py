from sortedcontainers import SortedList

vals = [1,2,3,4,5,6,7,8]

s = SortedList(key=lambda d: vals[d])



s.add(1)
s.add(2)
s.add(5)
s.add(4)


print(s[2])