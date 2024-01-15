from typing import List
from bisect import bisect_left


class Solution:
    def kmp_search(self, text, pattern):
        m = len(pattern)
        pi = [0] * m
        c = 0
        for i in range(1, m):
            v = pattern[i]
            while c and pattern[c] != v:
                c = pi[c - 1]
            if pattern[c] == v:
                c += 1
            pi[i] = c

        res = []
        c = 0
        for i, v in enumerate(text):
            while c and pattern[c] != v:
                c = pi[c - 1]
            if pattern[c] == v:
                c += 1
            if c == len(pattern):
                res.append(i - m + 1)
                c = pi[c - 1]
        return res

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