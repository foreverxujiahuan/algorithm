from collections import Counter, defaultdict
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        length_p = len(p)
        length_s = len(s)
        p_counter = dict()
        cur_counter = dict()
        for ch in set(s+p):
            p_counter[ch] = 0
            cur_counter[ch] = 0
        for ch in p:
            p_counter[ch] += 1
        for ch in s[: length_p]:
            cur_counter[ch] += 1
        ans = []
        for i in range(length_p, length_s):
            if cur_counter == p_counter:
                ans.append(i - length_p)
            cur_counter[s[i]] += 1
            cur_counter[s[i - length_p]] -= 1
        if cur_counter == p_counter:
            ans.append(length_s - length_p)
        return ans


if __name__ == '__main__':
    s = "aa"
    p = "bb"
    solution = Solution()
    res = solution.findAnagrams(s, p)
    print(res)
