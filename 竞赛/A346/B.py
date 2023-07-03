class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        tmp = list(s)
        length = len(s)
        if length % 2 != 0:
            mid = (length // 2)
            l, r = mid-1, mid + 1
        else:
            mid = length // 2
            l, r = mid-1, mid
        while l != -1 and r != length:
            if s[l] != s[r]:
                tmp[l] = min(s[l], s[r])
                tmp[r] = min(s[l], s[r])
            l -= 1
            r += 1
        return "".join(tmp)


if __name__ == '__main__':
    solution = Solution()
    s = "seven"
    res = solution.makeSmallestPalindrome(s)
    print(res)