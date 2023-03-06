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
    candidates1 = {2 ** i for i in range(18)}
    candidates2 = {-(2 ** i) for i in range(18)}
    candidates = list(candidates1.union(candidates2))
    # target = 8
    # solution = Solution()
    # ans = solution.combinationSum(candidates, target)
    # print(ans)
    solution = Solution()
    candidates = [64, 1, 2, 8]
    target = 8
    ans = solution.combinationSum(candidates, target)
    print(ans)
