from typing import List


class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        f = [True] + [False] * n
        for i, x in enumerate(nums):
            flag1 = i > 0 and f[i - 1] and x == nums[i - 1]  # x 和前面的数字相同
            flag2 = i > 1 and f[i - 2] and (x == nums[i - 1] == nums[i - 2] or
                                            x == nums[i - 1] + 1 == nums[i - 2] + 2)  # 前面三个数字是顺子
            if flag1 or flag2:
                f[i + 1] = True
        return f[n]


if __name__ == '__main__':
    solution = Solution()
    nums = [1,2,3,3]
    res = solution.validPartition(nums)
    print(res)
