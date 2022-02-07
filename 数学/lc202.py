class Solution:
    def isHappy(self, n: int) -> bool:
        while not self.flag(n):
            outout = 0
            nums = [int(t) for t in list(str(n))]
            if len(nums) == 1 and nums[0] != 1 and nums[0] != 7:
                return False
            for t in nums:
                outout += t * t
            nums = [int(t) for t in list(str(outout))]
            n = int(''.join([str(t) for t in nums]))
        return True

    def flag(self, n):
        nums = [int(t) for t in list(str(n))]
        res = 0
        for t in nums:
            res += t*t
        return res == 1

n = 7
solution = Solution()
res = solution.isHappy(n)
print(res)
