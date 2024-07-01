# import random
#
#
# lst = [random.randint(0, 10000) for _ in range(100)]
#
# lst.sort()
# print(lst)
#
# target = 3772
#
# #
# # # if n == target:
# # #     pass
# # for i in range(100):
# #     if lst[i] == target:
# #         print("yes")
# #     else:
# #         print("No")
#
#
# # mid_index = 50
# # mid_num = lst[50]
# # print(mid_num)
# # mid_index = 25
# # mid_num2 = lst[25]
# # 50, 25, 37, 42, 45, 47, 48, 49
# # log2,4 = 2
# # log2N, 2的几次方=N; y = log2N -> 2 ** y = N;N为lst的长度
# print(2 ** 7)
# m = 10000  # 行的数量
# n = 10000  # 列的数量
# # 暴力查找，exhasutive search,需要查找10000次; O(r*c)
# # 对于每一行，进行一个二分查找, log2,n; m * 13; O()
# # 空间复杂度:是算法额外占用了多少内存; O(1); O(2*r*c) = O(r*c) = O(3 * r * c)
# # O(1)，额外占用常数量的空间复杂度；占用的内存大小和输入数据的尺寸无关
#
# import math
# print(math.log(10000, 2))
#
# # O(m+n)

import random
lst = [random.randint(0, 10000) for _ in range(100)]
target = random.choice(lst)
lst.sort()
print(f"lst:{lst}")
print(f"target:{target}")
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
