from typing import List


class Solution:
    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        n = len(arr)
        pos = [i for i in range(n) if arr[i] == 1]
        m = len(pos)
        presum = [0] * (m + 1)
        for i in range(m):
            presum[i + 1] = presum[i] + pos[i]
        ans = float('inf')
        for i in range(m - k + 1):
            mid = i + (k - 1) // 2
            left_sum = presum[mid] - presum[i] - (mid - i) * pos[mid]
            right_sum = presum[i + k] - presum[mid + 1] - (i + k - 1 - (mid + 1)) * pos[mid + 1]
            ans = min(ans, left_sum + right_sum)
        return ans

if __name__ == '__main__':
    arr = [1,7,9,6]
    k = 1
    solution = Solution()
    res = solution.makeSubKSumEqual(arr, k)
    print(res)