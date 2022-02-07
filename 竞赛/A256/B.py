from typing import List


class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums = [int(n) for n in nums]
        nums.sort()
        return str(nums[len(nums) - k])


if __name__ == '__main__':
    nums = ['0', '0']
    k = 2
    s = Solution()
    res = s.kthLargestNumber(nums, k)
    print(res)