class Solution:
    def minimumBeautifulSubstrings(self, s: str) -> int:
        candidates = [str(bin(5 ** i))[2:] for i in range(10, -1, -1)]
        n = len(s)
        cnt = 0
        for candidate in candidates:
            if candidate in s:
                cnt += s.count(candidate)
                s = s.replace(candidate, "2" * len(candidate))
        if s != "2" * n:
            return -1
        return cnt

if __name__ == '__main__':
    s = "101101111101"
    solution = Solution()
    res = solution.minimumBeautifulSubstrings(s)
    print(res)
    # for i in range(10):
    #     print(bin(5 ** i))