from typing import List


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums2index = dict()
        for i, n in enumerate(nums):
            cur = target - n  # 当前需要寻找的数字
            if cur in nums2index.keys() and i != nums2index[cur]:
                return [i, nums2index[cur]]
            nums2index[n] = i
        return []


d = {
    2: 0,
    7: 1
}

if __name__ == '__main__':
    nums = [2,7,11,15]
    target = 13
    solution = Solution()
    res = solution.twoSum(nums, target)
    print(res)