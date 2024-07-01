from typing import List


class Solution:
    def maximumTotalCost(self, nums: List[int]) -> int:
        pos_sum = sum([n for n in nums if n > 0])
        neg_sub_arr = []
        cur_neg_sub_arr = []
        length = len(nums)
        if length == 1:
            return nums[0]
        single_neg_sum = 0
        for i in range(1, length-1):
            if nums[i] < 0 and nums[i-1] >= 0 and nums[i+1] >= 0:
                single_neg_sum += - nums[i]
        if nums[0] < 0 and nums[1] > 0:
            single_neg_sum += nums[0]
        if nums[-1] < 0 and nums[-2] > 0:
            single_neg_sum -= nums[-1]
        for i in range(length):
            if nums[i] <= 0:
                cur_neg_sub_arr.append(nums[i])
            else:
                if len(cur_neg_sub_arr) >= 2:
                    neg_sub_arr.append(cur_neg_sub_arr)
                cur_neg_sub_arr = []
        if len(cur_neg_sub_arr) >= 2:
            neg_sub_arr.append(cur_neg_sub_arr)
        neg_sum = sum([self.get_max_sum(sub_arr) for sub_arr in neg_sub_arr])
        return pos_sum + neg_sum + single_neg_sum

    def get_max_sum(self, arr):
        length = len(arr)
        ans1 = 0
        flag = 1
        for i in range(length):
            ans1 += arr[i] * flag
            flag *= -1
        ans2 = arr[0]
        flag = 1
        for i in range(1, length):
            ans2 += arr[i] * flag
            flag *= -1
        return max(ans1, ans2)


if __name__ == '__main__':
    solution = Solution()
    nums = [1, -5, -2]
    res = solution.maximumTotalCost(nums)
    print(res)