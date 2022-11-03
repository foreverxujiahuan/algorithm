import math

class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        nums = list(str(n))
        length = len(nums)
        i = len(nums) - 1
        while sum([int(i) for i in nums]) > target:
            diff = 10 - int(nums[i])
            nums = int("".join(nums)) + diff * int(math.pow(10, length-i - 1))
            nums = list(str(nums))
            i -= 1
        return int("".join(nums)) - n


if __name__ == '__main__':
    solution = Solution()
    n = 1
    target = 1
    res = solution.makeIntegerBeautiful(n, target)
    print(res)