from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        ans = ''
        keys = sorted(list(counter.keys()), key=lambda c:counter[c], reverse=True)
        for k in keys:
            ans += k * counter[k]
        return ans
