from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        new_nums = []
        pos_nums = []
        neg_nums = []
        for n in nums:
            if n > 0:
                pos_nums.append(n)
            else:
                neg_nums.append(n)
        for i in range(len(pos_nums)):
            new_nums.append(pos_nums[i])
            new_nums.append(neg_nums[i])
        return new_nums

if __name__ == '__main__':
    nums = [3,1,-2,-5,2,-4]
    solution = Solution()
    res = solution.rearrangeArray(nums)
    print(res)