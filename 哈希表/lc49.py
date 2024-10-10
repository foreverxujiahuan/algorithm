from collections import Counter
from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            counter = Counter(s)
            ch2cnt = ""
            for k, v in sorted(counter):
                ch2cnt += k + str(v)
            d[ch2cnt].append(s)
        return list(d.values())


