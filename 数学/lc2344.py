from typing import List


class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        ans = 0
        nums.sort()
        visited = set()
        length = len(nums)
        numsDivide = set(numsDivide)
        for n in nums:
            if n in visited:
                ans += 1
                continue
            flag = 1
            for num in numsDivide:
                if num % n != 0:
                    ans += 1
                    flag = 0
                    break
            if flag == 1:
                break
        if ans == length:
            return -1
        return ans

if __name__ == '__main__':
    solution = Solution()
    nums = [2,3,2,4,3]
    numsDivide = [9,6,9,3,15]
    res = solution.minOperations(nums, numsDivide)
    print(res)

