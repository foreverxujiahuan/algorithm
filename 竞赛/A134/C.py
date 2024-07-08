from typing import List


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        s = "".join([str(t) for t in colors])
        tmp1 = "".join([str(t) for t in colors[-(k-1):]])
        s = tmp1 + s
        ans = 0
        length = len(s)
        cur = 1
        for i in range(length-1):
            if s[i] != s[i+1]:
                cur += 1
            else:
                if cur >= k:
                    ans += cur - k + 1
                cur = 1
        if cur >= k:
            ans += cur - k + 1
        return ans



if __name__ == '__main__':
    solution = Solution()
    # colors = [0,1,0,0,1,0,1]
    # k = 6
    # colors = [0,1,0,1,0]
    # k = 3
    # colors = [1, 1, 0, 1]
    # k = 4
    colors = [0,0,1]
    k = 3
    res = solution.numberOfAlternatingGroups(colors, k)
    print(res)