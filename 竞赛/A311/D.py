from collections import Counter
from typing import List


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        ans = []
        d = dict()
        for word in words:
            t = ''
            for s in word:
                t += s
                if t in d.keys():
                    d[t] += 1
                else:
                    d[t] = 1
        length = len(words)
        for i in range(length):
            t = 0
            word = words[i]
            for j in range(1, len(words[i]) + 1):
                cur_s = word[: j]
                t += d[cur_s]
            ans.append(t)
        return ans


if __name__ == '__main__':
    words = ["abc", "ab", "bc", "b"]
    solution = Solution()
    res = solution.sumPrefixScores(words)
    print(res)