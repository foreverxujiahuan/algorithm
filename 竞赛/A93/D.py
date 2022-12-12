from typing import List


class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        mx = -1
        for s in strs:
            if s.isdigit():
                mx = max(mx, int(s))
            else:
                mx = max(mx, len(s))
        return mx