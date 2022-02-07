from typing import List


class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        res = 0
        length = len(nums)
        dp_max = [0 for _ in range(length)]
        dp_min = [0 for _ in range(length)]
        dp_max[0] = nums[0]
        dp_min[length - 1] = nums[-1]
        for i in range(1, length):
            if nums[i] > dp_max[i - 1]:
                dp_max[i] = nums[i]
            else:
                dp_max[i] = dp_max[i - 1]
        for i in range(length - 2, -1, -1):
            if nums[i] < dp_min[i + 1]:
                dp_min[i] = nums[i]
            else:
                dp_min[i] = dp_min[i + 1]
        for i in range(1, length - 1):
            if dp_max[i - 1] < nums[i] < dp_min[i+1]:
                res += 2
                continue
            if nums[i - 1] < nums[i] < nums[i + 1]:
                res += 1
        return res


if __name__ == '__main__':
    s = Solution()
    nums = [3,48,33,17,21,95,24,67,89,1,50,76,6,32,20,5,1,45,79,81,96,96,15,37,44,63,4,40,58,71,99,78,95,6,34,97,52,80,91,20,61,29,12,85,88,41,14,4,58,17,67,75,100,51,63,66,42,19,44,34,34,78,54,84,3,90,72,18,86,8,33,5,17,21,22,13,59,82,30,66,91,5,32,30,92,57,10,33,11,76,30,80,80,91,47,33]
    res = s.sumOfBeauties(nums)
    print(res)



