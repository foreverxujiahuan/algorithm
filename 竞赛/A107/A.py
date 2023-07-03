from typing import List


class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        ans = 0
        length = len(words)
        for i in range(length):
            for j in range(i+1, length):
                if words[i][0] == words[j][1] and words[j][0] == words[i][1]:
                    ans += 1
        return ans


