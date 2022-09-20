from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 0
        ans = None
        for n in nums:
            if cnt == 0:
                ans = n
            if n == ans:
                cnt += 1
            else:
                cnt -= 1
        return ans


if __name__ == '__main__':
    solution = Solution()
    nums = [2,2,1,1,1,2,2]
    res = solution.majorityElement(nums)
    print(res)

