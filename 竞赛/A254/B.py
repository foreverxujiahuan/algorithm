from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        length = len(nums)
        m = (length + 1) // 2
        res = []
        for i in range(m):
            res.append(nums[i])
            if i+m < length:
                res.append(nums[i+m])
        return res


if __name__ == '__main__':
    nums = [1,2,3,4,5]
    s = Solution()
    res = s.rearrangeArray(nums)
    print(res)
