from typing import List


class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        ans = 99999
        length = len(nums)
        for i in range(1, length):
            for j in range(i+1, length):
                sub1 = nums[:i]
                sub2 = nums[i:j]
                sub3 = nums[j:]
                if sub1 and sub2 and sub3:
                    ans = min(ans, sub1[0] + sub2[0] + sub3[0])
        return ans

if __name__ == '__main__':
    nums = [10,3,1,1]
    solution = Solution()
    res = solution.minimumCost(nums)
    print(res)