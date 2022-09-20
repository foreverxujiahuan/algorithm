from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        s = set()
        length = len(nums)
        for i in range(length):
            target = -nums[i]
            l, r = i+1, length-1
            while l < r:
                if nums[l] + nums[r] > target:
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    t = sorted([nums[i], nums[l], nums[r]])
                    if l != r and l != i and r != i and tuple(t) not in s:
                        s.add(tuple(sorted([nums[i], nums[l], nums[r]])))
                        ans.append(t)
                    l += 1
                    r -= 1
        return ans


if __name__ == '__main__':
    nums = [1,2,-2,-1]
    solution = Solution()
    res = solution.threeSum(nums)
    print(res)
