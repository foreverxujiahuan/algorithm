from typing import List


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        import heapq
        n = len(piles)
        # 生成最大堆
        for i in range(n):
            piles[i] = -piles[i]
        heapq.heapify(piles)
        for i in range(k):
            # 单次操作：记录并弹出最大值，修改后重新添加进堆
            tmp = heapq.heappop(piles)
            heapq.heappush(piles, tmp + (-tmp) // 2)
        return -sum(piles)


if __name__ == '__main__':
    solution = Solution()
    piles = [4,3,6,7]
    k = 3
    res = solution.minStoneSum(piles, k)
    print(res)
