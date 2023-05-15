from typing import List


class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        scores = [0 for _ in range(n)]
        scores[0] = 1
        i = 1
        cur = 0
        while scores.count(2) == 0:
            index = (i * k + cur) % n
            scores[index] += 1
            i += 1
            cur = index
        ans = [i+1 for i in range(len(scores)) if scores[i] == 0]
        return ans


if __name__ == '__main__':
    n = 4
    k = 4
    solution = Solution()
    res = solution.circularGameLosers(n, k)
    print(res)
