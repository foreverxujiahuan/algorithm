from collections import Counter
from typing import List


def combinationSum2(candidates: List[int], target: int) -> List[List[int]]:
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
    candidates = [(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(1,2),(1,2),(1,2),(2,3),(2,3)]
    target = 6
    ans = combinationSum2(candidates, target)
    print(ans)