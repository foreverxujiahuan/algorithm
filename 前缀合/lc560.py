from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre_sum = [nums[0]]
        length = len(nums)
        for i in range(1, length):
            pre_sum.append(pre_sum[-1] + nums[i])
        res = 0
        for i in range(length):
            if pre_sum[i] == k:
                res += 1
            for j in range(i + 1, length):
                if pre_sum[j] - pre_sum[i] == k:
                    res += 1
                    break
        return res

if __name__ == '__main__':
    solution = Solution()
    nums = [1, 1, 1]
    k = 2
    res = solution.subarraySum(nums, k)
    print(res)