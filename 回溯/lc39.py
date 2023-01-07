from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        cur = []
        ans = []
        def dfs(n, target, s, index):
            if s == target:
                ans.append(cur[:])
                return
            if s > target:
                return
            for i in range(index, n):
                cur.append(candidates[i])
                s += candidates[i]
                dfs(n, target, s, i)
                s -= candidates[i]
                cur.pop()
        s = 0
        index = 0
        length = len(candidates)
        dfs(length, target, s, index)
        return ans


if __name__ == '__main__':
    solution = Solution()
    candidates = [2, 3, 5]
    target = 8
    res = solution.combinationSum(candidates, target)
    print(res)