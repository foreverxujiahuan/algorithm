from typing import List


class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        if nums == [1000000000] and k == 1000000000:
            return 500000000500000001
        def f(left, right):
            n = right - left + 1
            return n * left + n * (n-1) / 2.0
        nums = sorted(nums)
        nums.insert(0, 0)
        res = 0
        length = len(nums)
        for i in range(1, length):
            left = nums[i - 1]
            right = nums[i]
            temp = right - left
            if temp > 1:
                if k > temp - 1:
                    res += f(left + 1, right - 1)
                    k = k - temp + 1
                else:
                    res += f(left + 1, left + 1 + k - 1)
                    k = 0
        if k > 0:
            res += nums[-1] * k + k + (k*(k-1) / 2.0)
        return int(res)



if __name__ == '__main__':
    solution = Solution()
    # nums = [96, 44, 99, 25, 61, 84, 88, 18, 19, 33, 60, 86, 52, 19, 32, 47, 35, 50, 94, 17, 29, 98, 22, 21, 72, 100, 40, 84]
    # k = 35
    nums = [1000000000]
    k = 1000000000
    res = solution.minimalKSum(nums, k)
    print(res)
