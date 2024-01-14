from typing import List


class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        ans = -1
        mx = 0
        for x, y in dimensions:
            if x ** 2 + y ** 2 > mx:
                mx = x ** 2 + y ** 2
                ans = x * y
            if x ** 2 + y ** 2 == mx and x * y > ans:
                ans = x * y
        return ans

if __name__ == '__main__':
    solution = Solution()
    dimensions = [[3,4],[4,3]]
    res = solution.areaOfMaxDiagonal(dimensions)
    print(res)
