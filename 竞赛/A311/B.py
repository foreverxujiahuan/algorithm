class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        i, j = 0, 0
        max_length = 1
        length = len(s)
        while j < length-1:
            if ord(s[j+1]) == ord(s[j]) + 1:
                j += 1
                max_length = max(max_length, j-i+1)
            else:
                i, j = j+1, j+1
        return max_length


if __name__ == '__main__':
    s = "ab"
    solution = Solution()
    res = solution.longestContinuousSubstring(s)
    print(res)