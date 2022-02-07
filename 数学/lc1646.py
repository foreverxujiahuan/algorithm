

class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        nums = [0 for _ in range(n+1)]
        nums[0] = 0
        nums[1] = 1
        for i in range(n):
            if 2 <= 2 * i <= n:
                nums[2 * i] = nums[i]
            if 2 <= 2 * i + 1 <= n:
                nums[2 * i + 1] = nums[i] + nums[i + 1]
        return max(nums)


if __name__ == '__main__':
    s = Solution()
    n = 0
    res = s.getMaximumGenerated(n)
    print(res)