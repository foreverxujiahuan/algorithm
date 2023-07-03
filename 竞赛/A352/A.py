from typing import List


class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        length = len(nums)
        ans = 0
        for l in range(length):
            for r in range(l+1, length+1):
                sub = nums[l: r]
                flag = self.f(sub, threshold)
                if flag:
                    ans = max(ans, r-l)
        return ans

    def f(self, sub, threshold):
        l = 0
        r = len(sub)
        length = len(sub)
        if not sub[l] % 2 == 0:
            return False
        for i in range(l, r):
            if i != length - 1 and not sub[i] % 2 != sub[i + 1] % 2:
                return False
        for i in range(l, r):
            if sub[i] > threshold:
                return False
        return True

if __name__ == '__main__':
    nums = [3,2,5,4]
    threshold = 5
    solution = Solution()
    res = solution.longestAlternatingSubarray(nums, threshold)
    print(res)