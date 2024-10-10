from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter1 = Counter(ransomNote)
        counter2 = Counter(magazine)
        for k, v in counter1.items():
            if k not in counter2 or counter2[k] < v:
                return False
        return True
