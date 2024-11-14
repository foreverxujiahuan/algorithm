from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        ans = 0
        index = 0
        for c in g:
            while index < len(s):
                if s[index] >= c:
                    ans += 1
                    index += 1
                    break
                else:
                    index += 1
        return ans


if __name__ == '__main__':
    solution = Solution()
    g = [10,9,8,7]
    s = [5,6,7,8]
    res = solution.findContentChildren(g, s)
    print(res)