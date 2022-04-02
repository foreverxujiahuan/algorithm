import bisect

nums = [1,2,3,4,5,6]

# 获取目标数字的坐标
index_right = bisect.bisect_right(nums, 3.2)
index_left = bisect.bisect_left(nums, 3.2)
print(index_right)
print(index_left)

