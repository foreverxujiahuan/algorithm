from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        mx = 0
        while l < r:
            if height[l] < height[r]:
                cur = (r - l) * height[l]
                l += 1
            else:
                cur = (r - l) * height[r]
                r -= 1
            mx = max(cur, mx)
        return mx


if __name__ == '__main__':
    solution = Solution()
    height = [1, 1]
    res = solution.maxArea(height)
    print(res)