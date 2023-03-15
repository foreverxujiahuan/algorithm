from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        length = len(nums)
        right_most = 0
        for i in range(length):
            if i <= right_most:
                right_most = max(right_most, i + nums[i])
            if right_most >= length - 1:
                return True
        return False


if __name__ == '__main__':
    s = Solution()
    nums = [3,2,1,0,4]
    res = s.canJump(nums)
    print(res)