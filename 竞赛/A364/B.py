from typing import List


class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        length = len(maxHeights)
        ans = 0
        for mid in range(length):
            ans = max(self.f(maxHeights, mid), ans)
        return ans

    def f(self, maxHeights: List[int], mid) -> int:
        height = [1e1000 for _ in maxHeights]
        length = len(maxHeights)
        height[mid] = maxHeights[mid]
        for i in range(mid - 1, -1, -1):
            height[i] = min(height[i + 1], maxHeights[i])
        for i in range(mid + 1, length):
            height[i] = min(height[i - 1], maxHeights[i])
        return sum(height)



if __name__ == '__main__':
    maxHeights = [3,2,5,5,2,3]
    solution = Solution()
    res = solution.maximumSumOfHeights(maxHeights)
    print(res)