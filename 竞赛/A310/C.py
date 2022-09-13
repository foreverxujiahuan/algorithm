from heapq import heapreplace, heappush
from typing import List
import bisect


class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        h = []
        for left, right in intervals:
            if h and left > h[0]:
                heapreplace(h, right)
            else:
                heappush(h, right)
        return len(h)



if __name__ == '__main__':
    intervals = [[5,10],[6,8],[1,5],[2,3],[1,10]]

    solution = Solution()
    res = solution.minGroups(intervals)
    print(res)
