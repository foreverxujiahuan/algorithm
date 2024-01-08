from typing import List
from itertools import accumulate
from sklearn.metrics import classification_report


class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        max_values = sorted(maxHeights, reverse=True)[:10]
        max_values = set(max_values)

        length = len(maxHeights)
        if len(maxHeights) > 500:
            candidate_index = [maxHeights.index(v) for v in max_values]
            for v in max_values:
                for i in range(length-1, -1, -1):
                    if maxHeights[i] == v:
                        candidate_index.append(i)
                        break
        else:
            candidate_index = []
            for i in range(len(maxHeights)):
                if maxHeights[i] in max_values:
                    candidate_index.append(i)
        ans = 0
        for mid in candidate_index:
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
    maxHeights = [5,3,4,1,1]
    solution = Solution()
    res = solution.maximumSumOfHeights(maxHeights)
    print(res)