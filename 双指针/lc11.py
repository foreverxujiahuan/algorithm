from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        candidate = []
        right = len(height) - 1
        left = 0
        while left < right:
            if height[left] < height[right]:
                t = (right - left) * min(height[left], height[right])
                candidate.append(t)
                left += 1
            else:
                t = (right - left) * min(height[left], height[right])
                candidate.append(t)
                right -= 1
        return max(candidate)


if __name__ == '__main__':
    solution = Solution()
    height = [1,8,6,2,5,4,8,3,7]
    res = solution.maxArea(height)
    print(res)