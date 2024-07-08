from typing import List


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        s = "".join([str(t) for t in colors])
        s = str(colors[-1]) + s + str(colors[0])
        ans = 0
        for i in range(len(s) - 2):
            if s[i:i+3] in {"010", "101"}:
                ans += 1

        return ans


if __name__ == '__main__':
    solution  = Solution()
    colors = [0,1,0,1]
    res = solution.numberOfAlternatingGroups(colors)
    print(res)