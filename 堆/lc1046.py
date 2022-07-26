import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        # 模拟
        while len(heap) > 1:
            x, y = heapq.heappop(heap), heapq.heappop(heap)
            if x != y:
                heapq.heappush(heap, x - y)

        if heap:
            return -heap[0]
        return 0


if __name__ == '__main__':
    stones = [2, 7, 4, 1, 8, 1]
    solution = Solution()
    res = solution.lastStoneWeight(stones)
    print(res)



