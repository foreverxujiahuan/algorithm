import heapq

import collections

class SmallestInfiniteSet:

    def __init__(self):
        self.nums = list(range(1024))
        heapq.heapify(self.nums)

    def popSmallest(self) -> int:
        return heapq.heappop(self.nums)

    def addBack(self, num: int) -> None:
        if num not in self.nums:
            heapq.heappush(self.nums, num)
