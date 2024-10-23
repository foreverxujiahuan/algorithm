from typing import List


class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        t1 = [nums[0], nums[1], nums[2]]
        t2 = [nums[0], nums[2], nums[1]]
        t3 = [nums[1], nums[2], nums[0]]
        t4 = [nums[1], nums[0], nums[2]]
        t5 = [nums[2], nums[1], nums[0]]
        t6 = [nums[2], nums[0], nums[1]]
        return max([self.f(t1),self.f(t2),self.f(t3),self.f(t4),self.f(t5),self.f(t6)])


    def f(self,nums):
        bin_str = ""
        for n in nums:
            bin_n = bin(n)[2:]
            bin_str += bin_n
        flag = 1
        ans = 0
        for c in reversed(bin_str):
            if c == '1':
                ans += flag
            flag *= 2
        return ans

if __name__ == '__main__':
    solution = Solution()
    res = solution.maxGoodNumber(nums=[1,2,3])
    print(res)