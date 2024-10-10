from collections import Counter
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target_counter = Counter(p)
        ans = []
        length = len(p)
        cur = s[:length]
        cur_counter = Counter(cur)
        if cur_counter == target_counter:
            ans.append(0)
        for i in range(length, len(s)):
            cur_counter[s[i]] += 1
            cur_counter[s[i-length]] -= 1
            if cur_counter[s[i-length]] == 0:
                del cur_counter[s[i-length]]
            if cur_counter == target_counter:
                ans.append(i-length+1)
        return ans


if __name__ == '__main__':
    solution = Solution()
    s = "abab"
    p = "ab"
    res = solution.findAnagrams(s, p)
    print(res)
