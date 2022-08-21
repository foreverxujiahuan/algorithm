class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        ans = 0
        while '01' in s:
            s = s.replace("01", "10")
            ans += 1
        return ans

if __name__ == '__main__':
    solution = Solution()
    s = "11100"
    res = solution.secondsToRemoveOccurrences(s)
    print(res)