from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        length = len(nums)
        res = []
        for i in range(length):
            left = i + 1
            right = length - 1
            target = -nums[i]
            while left < right:
                if nums[left] + nums[right] < target:
                    left += 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    temp = [nums[i], nums[left], nums[right]]
                    temp.sort()
                    if temp not in res:
                        res.append(temp)
                    left += 1
                    right -= 1
        res = list(res)
        return res

if __name__ == '__main__':
    nums = [-2,0,1,1,2]
    solution = Solution()
    res = solution.threeSum(nums)
    print(res)

