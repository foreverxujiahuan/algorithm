from typing import List


class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        points = set()
        for start, end in nums:
            cur = set(range(start, end+1))
            points.update(cur)
        return len(points)