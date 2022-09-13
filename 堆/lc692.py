from collections import Counter
from typing import List
import heapq


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        return [q[0] for q in heapq.nsmallest(n=k, iterable=counter.items(), key=lambda d: (-d[1], d[0]))]


if __name__ == '__main__':
    words = ["i","love","leetcode","i","love","coding"]
    k = 2
    solution = Solution()
    res = solution.topKFrequent(words, k)
    print(res)