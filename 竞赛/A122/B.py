from typing import List


class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        sub_nums = []
        length = len(nums)
        cur_sub = [nums[0]]
        cur_cnt = bin(nums[0]).count('1')
        for i in range(1, length):
            if bin(nums[i]).count('1') == cur_cnt:
                cur_sub.append(nums[i])
            else:
                sub_nums.append(cur_sub)
                cur_cnt = bin(nums[i]).count('1')
                cur_sub = [nums[i]]
        if cur_sub:
            sub_nums.append(cur_sub)
        tmp_nums = []
        for sub in sub_nums:
            tmp_nums.extend(sorted(sub))
        if tmp_nums == sorted(nums):
            return True
        return False

if __name__ == '__main__':
    solution = Solution()
    nums = [3,16,8,4,2]
    res = solution.canSortArray(nums)
    print(res)
