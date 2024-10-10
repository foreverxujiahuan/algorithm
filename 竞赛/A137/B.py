from typing import List


class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        ans = [-1] * (len(nums) - k + 1)
        cnt = 0
        for i, n in enumerate(nums):
            if i == 0 or nums[i] == nums[i-1] + 1:
                cnt += 1
            else:
                cnt = 1
            if cnt >= k:
                ans[i-k+1] = nums[i]
        return ans


if __name__ == '__main__':
    solution = Solution()


    nums = [3,2,3,2,3,2]
    k = 2
    res = solution.resultsArray(nums, k)
    print(res)