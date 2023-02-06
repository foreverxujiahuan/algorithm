from itertools import accumulate
from typing import List


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        s = {'a', 'e', 'i', 'o', 'u'}
        flags = [1 if word[0] in s and word[-1] in s else 0 for word in words]
        accsum = list(accumulate(flags))
        ans = []
        for query in queries:
            start, end = query
            if start == 0:
                cur = accsum[end]
            else:
                cur = accsum[end] - accsum[start - 1]
            ans.append(cur)
        return ans

if __name__ == '__main__':
    words = ["a","e","i"]
    queries = [[0,2],[0,1],[2,2]]
    solution = Solution()
    res = solution.vowelStrings(words, queries)
    print(res)