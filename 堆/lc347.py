import collections
from typing import List
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        heap = [(val, key) for key, val in count.items()]
        return [item[1] for item in heapq.nlargest(k, heap)]


if __name__ == '__main__':
    nums = [1,1,1,2,2,3]
    k = 2
    solution = Solution()
    res = solution.topKFrequent(nums, k)
    print(res)
