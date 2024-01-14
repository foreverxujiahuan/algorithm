from typing import List
from bisect import bisect_left
import re

class Solution:
    def build_lps(self, pattern):
        m = len(pattern)
        lps = [0] * m
        length = 0
        i = 1

        while i < m:
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1

        return lps

    def kmp_search(self, text, pattern):
        n = len(text)
        m = len(pattern)
        lps = self.build_lps(pattern)
        i = 0
        j = 0
        ans = []
        while i < n:
            if pattern[j] == text[i]:
                i += 1
                j += 1

            if j == m:
                ans.append(i - j)
                j = lps[j - 1]
            elif i < n and pattern[j] != text[i]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        return ans


    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        a_index = self.kmp_search(s, a)
        b_index = self.kmp_search(s, b)
        ans = []
        for i in a_index:
            candidate_index = bisect_left(b_index, i)
            if (candidate_index != len(b_index) and abs(b_index[candidate_index] - i) <= k) or \
                    (candidate_index != 0 and abs(b_index[candidate_index - 1] - i) <= k):
                ans.append(i)
        return ans


if __name__ == '__main__':
    solution = Solution()
    s = "isawsquirrelnearmysquirrelhouseohmy"
    a = "my"
    b = "squirrel"
    k = 15
    # s = "s" * (10**5)
    # a = "s" * (10 ** 5)
    # b = "s" * (10 ** 5)
    # k = 15
    # s = "abcd"
    # a = "a"
    # b = "a"
    # k = 4
    # s="vatevavakz"
    # a="va"
    # b="lbda"
    # k=1

    res = solution.beautifulIndices(s,a,b,k)
    print(res)