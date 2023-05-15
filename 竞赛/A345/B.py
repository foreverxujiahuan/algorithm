from typing import List


class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        if derived.count(1) % 2 == 0:
            return True
        return False

