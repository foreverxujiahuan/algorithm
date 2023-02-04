from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        length = len(nums)
        index1, index2 = -1, -1
        for i in range(length):
            if nums[i] != sorted_nums[i]:
                index1 = i
                break
        for j in range(length-1, -1, -1):
            if nums[j] != sorted_nums[j]:
                index2 = j
                break
        if index1 == -1:
            return 0
        return index2 - index1 + 1


if __name__ == '__main__':
    nums = [1]
    solution = Solution()
    res = solution.findUnsortedSubarray(nums)
    print(res)

