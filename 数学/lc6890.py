from typing import List


class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()
        length = len(nums)
        ans = min([abs(nums[i] - nums[i+1]) for i in range(length-1)])
        return ans


if __name__ == '__main__':
    solution = Solution()
    nums = [1,10,100]
    res = solution.findValueOfPartition(nums)
    print(res)