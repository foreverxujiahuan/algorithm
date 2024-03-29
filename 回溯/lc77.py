from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtracking(start):
            if len(path) == k:
                ans.append(path[:])
                return
            length = n - (k - len(path)) + 2
            for i in range(start, length):
                path.append(i)
                backtracking(i + 1)
                path.pop()

        path = []
        ans = []
        backtracking(1)
        return ans


if __name__ == '__main__':
    n = 4
    k = 2
    solution = Solution()
    res = solution.combine(n, k)
    print(res)
