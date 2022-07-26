from typing import List


class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        prefix_sum1 = [0]
        prefix_sum2 = [0]
        length = len(nums1)
        cur1, cur2 = 0, 0
        for i in range(length):
            cur1 += nums1[i]
            cur2 += nums2[i]
            prefix_sum1.append(cur1)
            prefix_sum2.append(cur2)
        t1 = self.get_max(prefix_sum1, prefix_sum2)
        t2 = self.get_max(prefix_sum2, prefix_sum1)
        return max(t1, t2)

    def get_max(self, prefix_sum1, prefix_sum2):
        i = 0
        j = i + 1
        length = len(prefix_sum1)
        t = 0
        while i < length and j < length:
            if prefix_sum1[j] - prefix_sum1[i] < prefix_sum2[j] - prefix_sum2[i]:
                t = max(t, (prefix_sum2[j] - prefix_sum2[i]) - (prefix_sum1[j] - prefix_sum1[i]))
                j += 1
            else:
                i = j
                j = i + 1

        return prefix_sum1[-1] + t




if __name__ == '__main__':
    solution = Solution()
    nums1 = [7,11,13]
    nums2 = [1,1,1]
    res = solution.maximumsSplicedArray(nums1, nums2)
    print(res)