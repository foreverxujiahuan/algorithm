from typing import List


class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        return sum([1 for t in patterns if t in word])
    