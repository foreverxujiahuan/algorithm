from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        l, r, ans = 1, n - 2, 0

        while l <= r:
            mid = l + r >> 1
            if arr[mid] > arr[mid + 1]:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1

        return ans


if __name__ == '__main__':
    solution = Solution()
    arr = [3,4,5,1]
    res = solution.peakIndexInMountainArray(arr)
    print(res)