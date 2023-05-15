from typing import List


class Solution:
    def sumOfPower(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        pre_sum = [nums[0]]
        s = nums[0]
        for i, n in enumerate(nums):
            if i == 0:
                continue
            else:
                pre_sum.append(s + n)
                s += pre_sum[-1]
        for i, n in enumerate(nums):
            ans += n * n * pre_sum[i]
            ans = ans % (10 ** 9 + 7)
        return ans


if __name__ == '__main__':
    solution = Solution()
    nums = [1,1,1]
    res = solution.sumOfPower(nums)
    print(res)