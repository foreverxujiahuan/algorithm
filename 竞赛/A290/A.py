from typing import List


class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        temp = set(nums[0])
        for t in nums:
            temp = temp.intersection(set(t))
        return list(sorted(temp))


if __name__ == '__main__':
    nums = [[1,2,3],[4,5,6]]
    solution = Solution()
    res = solution.intersection(nums)
    print(res)
