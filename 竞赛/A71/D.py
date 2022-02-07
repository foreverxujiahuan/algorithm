from typing import List


class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        length = len(nums)
        if length % 2 == 0:
            cnt = length // 6
            nums = sorted(nums)
            nums = nums[cnt:-cnt]
            temp_length = len(nums)
            first = []
            second = []
            for i in range(temp_length):
                if i % 2 == 0:
                    first.append(nums[i])
                else:
                    second.append(nums[i])
            return sum(first) - sum(second)
        else:
            cnt = length // 6
            nums = sorted(nums)
            nums1 = nums[cnt+1:-cnt]
            temp_length1 = len(nums1)
            first1 = []
            second1 = []
            for i in range(temp_length1):
                if i % 2 == 0:
                    first1.append(nums1[i])
                else:
                    second1.append(nums1[i])
            nums2 = nums[cnt:-cnt+1]
            temp_length2 = len(nums2)
            first2 = []
            second2 = []
            for i in range(temp_length2):
                if i % 2 == 0:
                    first2.append(nums2[i])
                else:
                    second2.append(nums2[i])
            return min(sum(first1) - sum(second2), sum(first2) - sum(second2))


if __name__ == '__main__':
    nums = [7,9,5,8,1,3]
    solution = Solution()
    res = solution.minimumDifference(nums)
    print(res)