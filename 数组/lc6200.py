from typing import List


class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        ans = -1
        pre = 0
        max_value = 0
        for log in logs:
            i, cur = log
            if cur - pre > max_value or (cur - pre == max_value and i < ans):
                ans = i
                max_value = cur - pre
            pre = cur
        return ans

if __name__ == '__main__':
    n = 2
    logs = [[0,10],[1,20]]
    solution = Solution()
    res = solution.hardestWorker(n, logs)
    print(res)
