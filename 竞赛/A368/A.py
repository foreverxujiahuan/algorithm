from typing import List


class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        length = len(nums)
        ans = 9999999999999
        for i in range(length):
            for j in range(i+1, length):
                for k in range(j+1, length):
                    if nums[i] < nums[j] and nums[j] > nums[k]:
                        ans = min(ans, nums[i] + nums[j] + nums[k])
        if ans == 9999999999999:
            ans = -1
        return ans


if __name__ == '__main__':
    print("1")