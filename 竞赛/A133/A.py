from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ans = 0
        for n in nums:
            if n % 3 == 0:
                ans += 0
            elif (n+1) % 3 == 0 or (n-1) % 3 == 0:
                ans += 1
        return ans


if __name__ == '__main__':
    nums = [3,6,9]
    solution = Solution()
    res = solution.minimumOperations(nums)
    print(res)