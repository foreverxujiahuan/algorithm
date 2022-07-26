from collections import Counter
from typing import List


class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        d = Counter(ranks)
        m = max(d.values())
        if len(set(suits)) == 1:
            return "Flush"
        elif m >= 3:
            return "Three of a Kind"
        elif m == 2:
            return "Pair"
        else:
            return "High Card"

if __name__ == '__main__':
    solution = Solution()
    ranks = [10,10,2,12,9]
    suits = ["a","b","c","a","d"]
    res = solution.bestHand(ranks, suits)
    print(res)