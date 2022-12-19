from typing import List


class Solution:
    def similarPairs(self, words: List[str]) -> int:
        ans = 0
        length = len(words)
        for i in range(length):
            for j in range(i+1, length):
                if set(words[i]) == set(words[j]):
                    ans += 1
        return ans
