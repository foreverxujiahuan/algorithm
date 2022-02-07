from typing import List


class Solution:

    def countKDifference(self, nums: List[int], k: int) -> int:
        length = len(nums)
        res = 0
        for i in range(length):
            for j in range(i+1, length):
                if abs(nums[j] - nums[i]) == k:
                    res += 1
        return res


if __name__ == '__main__':
    nums = [3,2,1,5,4]
    k = 2
    s = Solution()
    res = s.countKDifference(nums, k)
    print(res)