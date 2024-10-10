from typing import List


class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        ans = []
        length = len(nums)
        for i in range(length-k+1):
            cur = nums[i:i+k]
            if self.f(cur):
                ans.append(max(cur))
            else:
                ans.append(-1)
        return ans

    def f(self, sub_nums):
        for i in range(len(sub_nums) - 1):
            if sub_nums[i] == sub_nums[i+1] - 1:
                return False
        return True

if __name__ == '__main__':
    solution = Solution()


    nums = [2,2,2,2,2]
    k = 4
    res = solution.resultsArray(nums, k)
    print(res)