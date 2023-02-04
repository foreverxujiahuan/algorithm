from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        length = len(nums)
        for i in range(length-1):
            l, r = i+1, length - 1
            target = - nums[i]
            while l < r:
                if nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    if [nums[i], nums[l], nums[r]] not in ans:
                        ans.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
        return ans


if __name__ == '__main__':
    nums = [0,1,1]
    solution = Solution()
    res = solution.threeSum(nums)
    print(res)

