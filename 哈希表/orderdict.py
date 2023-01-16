from collections import Counter, OrderedDict

from sortedcontainers import SortedList

nums = [1,2,3,1,2,3,1]



counter = Counter(nums)

sl = SortedList()

tmp = counter.most_common()

print(tmp)

