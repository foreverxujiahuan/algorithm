from typing import List

from sortedcontainers import SortedList, SortedSet


class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        nums = SortedSet(nums)
        for mf, mt in zip(moveFrom, moveTo):
            nums.remove(mf)
            nums.add(mt)
        return sorted(list(set(nums)))


if __name__ == '__main__':
    nums = [1,1,3,3]
    moveFrom = [1,3]
    moveTo = [2,2]

    solution = Solution()
    res = solution.relocateMarbles(nums, moveFrom, moveTo)
    print(res)