

class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        chs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
               'o', 'p', 'q' , 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        ans = 0
        cur_s = ""
        for i in range(len(chs)):
            size = 0
            if chs[i] not in s:
                continue
            ans += chs[i]
            for j in range(len(s)):
                pass
            ans = max(ans, size)
        return ans

if __name__ == '__main__':
    # 5
    s = "eduktdb"
    k = 15
    # s = "acfgbd"
    # k = 2
    solution = Solution()
    res = solution.longestIdealString(s, k)
    print(res)