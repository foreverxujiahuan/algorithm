from math import sqrt
from typing import List


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for _ in range(k):
            i = gifts.index(max(gifts))
            gifts[i] = int(sqrt(gifts[i]))
        return sum(gifts)
