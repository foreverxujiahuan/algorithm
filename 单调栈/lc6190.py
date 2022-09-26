from typing import List


class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        f = [1 for _ in range(n)]
        g = [1 for _ in range(n)]
        for i in range(1, n):
            if nums[i] <= nums[i - 1]:
                f[i] = f[i - 1] + 1
            else:
                f[i] = 1
        for i in range(n - 1)[::-1]:
            if nums[i] <= nums[i + 1]:
                g[i] = g[i + 1] + 1
            else:
                g[i] = 1
        ans = []
        for i in range(k, n - k):
            if f[i - 1] >= k and g[i + 1] >= k:
                ans.append(i)
        return ans


if __name__ == '__main__':
    # nums = [878724,201541,179099,98437,35765,327555,475851,598885,849470,943442]
    # k = 4
    nums = [2, 1, 1, 1, 3, 4, 1]
    k = 2
    # nums = [2, 1, 1, 2]
    # k = 2
    # nums = [1,2,3]
    # k = 1
    # nums = [83441,339399,879745,789229,406453,100476,71931,60035,18971,172126,420833,798833,945593,987982,993320,994256,997289,998770]
    # k = 5
    solution = Solution()
    res = solution.goodIndices(nums, k)
    print(res)


