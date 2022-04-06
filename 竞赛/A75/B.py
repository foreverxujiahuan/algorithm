from typing import List


def triangularSum(nums: List[int]) -> int:
    length = len(nums)
    new_nums = [0] * (length - 1)
    if length == 1:
        return nums[0]
    while (len(nums) != 1):
        length = len(nums)
        new_nums = [0] * (length - 1)
        for i in range(length - 1):
            new_nums[i] = (nums[i] + nums[i + 1]) % 10
        nums = new_nums
    return new_nums[0]

nums = [5]
res = triangularSum(nums)
print(res)