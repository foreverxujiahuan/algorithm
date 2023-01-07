from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            d["".join(sorted(s))].append(s)
        return list(d.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
soltuion = Solution()
res = soltuion.groupAnagrams(strs)
print(res)
