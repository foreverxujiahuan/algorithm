class Solution:
    def maximumLength(self, s: str) -> int:
        length = len(s)
        ans = -1
        for i in range(length):
            for j in range(i+1, length+1):
                sub_s = s[i: j]
                if self.sub_s_count(s, sub_s) >= 3 and len(set(sub_s)) == 1:
                    ans = max(ans, len(sub_s))
        return ans


    def sub_s_count(self, s, sub_s):
        length = len(s)
        sub_length = len(sub_s)
        cnt = 0
        for i in range(length):
            if s[i:i+sub_length] == sub_s:
                cnt += 1
        return cnt

if __name__ == '__main__':
    s = "abcccccdddd"
    solution = Solution()
    res = solution.maximumLength(s)
    print(res)