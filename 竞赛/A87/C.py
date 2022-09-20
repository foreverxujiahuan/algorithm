from typing import List


class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        b = [0 for _ in range(32)]
        n = len(nums)
        ans = [0 for _ in range(n)]
        for i in range(n)[::-1]:
            for j in range(32):
                if nums[i] >> j & 1:
                    b[j] = i
            ans[i] = max(max(b) - i + 1, 1)
        return ans

    def smallestSubarrays2(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        ors = []  # 按位或的值 + 对应子数组的右端点的最小值
        for i in range(n - 1, -1, -1):
            num = nums[i]
            ors.append([0, i])
            k = 0
            for p in ors:
                p[0] |= num
                if ors[k][0] == p[0]:
                    ors[k][1] = p[1]  # 合并相同值，下标取最小的
                else:
                    k += 1
                    ors[k] = p
            del ors[k + 1:]
            # 本题只用到了 ors[0]，如果题目改成任意给定数值，可以在 ors 中查找
            ans[i] = ors[0][1] - i + 1
        return ans


if __name__ == '__main__':
    nums = [1,0,2,1,3]
    solution = Solution()
    res = solution.smallestSubarrays(nums)
    print(res)