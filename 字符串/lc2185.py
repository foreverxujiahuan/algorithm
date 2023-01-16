from typing import List


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return len([word for word in words if word.startswith(pref)])

