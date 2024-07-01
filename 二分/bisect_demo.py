import bisect

nums = [1,2,3,4,5,6]

# 获取目标数字的坐标
# index_right = bisect.bisect_right(nums, 3.2)
print(bisect.bisect_left(nums, 3))
# index_left = bisect.bisect_left(nums, 3.2)
# print(index_right)
# print(index_left)


import random
lst = [random.randint(0, 10000) for _ in range(100)]
target = random.choice(lst)
lst.sort()
print(f"lst:{lst}")
print(f"target:{target}")
# bisect.bisect_left
l, r = 0, len(lst)

while l < r:
    mid = (l + r) // 2
    if lst[mid] == target:
        print(f"mid:{mid}")
        break
    if lst[mid] < target:
        l = mid + 1
    else:
        r = mid
