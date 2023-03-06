from collections import Counter
from typing import List


class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        candidates = []
        for i, t in enumerate(types):
            candidates.extend([(i, t[1])] * t[0])
        temp = self.combinationSum2(candidates, target)
        mod = 10 ** 9 + 7
        ans = len(temp) % mod
        return ans

    def combinationSum2(self, candidates, target: int) -> List[List[int]]:
        def dfs(pos: int, rest: int):
            nonlocal sequence
            if rest == 0:
                ans.append(sequence[:])
                return
            if pos == len(freq) or rest < freq[pos][0][1]:
                return

            dfs(pos + 1, rest)

            most = min(rest // freq[pos][0][1], freq[pos][1])
            for i in range(1, most + 1):
                sequence.append(freq[pos][0][1])
                dfs(pos + 1, rest - i * freq[pos][0][1])
            sequence = sequence[:-most]

        freq = sorted(Counter(candidates).items())
        ans = list()
        sequence = list()
        dfs(0, target)
        return ans


if __name__ == '__main__':
    target = 500
    types = [[6,1],[49,2],[33,3],[26,4],[28,5],[45,6],[4,7],[23,8],[46,9],[39,10],[12,11],[28,12],[37,13],[18,14],[10,15],[27,16],[26,17],[10,18],[34,19],[11,20],[35,21],[5,22],[47,23],[19,24],[15,25],[27,26],[50,27],[3,28],[24,29],[18,30],[49,31],[32,32],[18,33],[5,34],[34,35]]
    solution = Solution()
    res = solution.waysToReachTarget(target, types)
    print(res)