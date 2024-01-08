from typing import List


class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        nums_set = set(nums)
        length = len(nums)
        sub_nums = [nums[0]]
        for i in range(1, length):
            if nums[i] == sub_nums[-1] + 1:
                sub_nums.append(nums[i])
            else:
                break
        s = sum(sub_nums)
        for i in range(s, 100000):
            if i not in nums_set:
                return i


if __name__ == '__main__':
    nums = [3,4,5,1,12,14,13]
    solution = Solution()
    res = solution.missingInteger(nums)
    print(res)

