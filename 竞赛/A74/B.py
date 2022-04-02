class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        s1 = pattern[0] + text
        cnt1 = 0
        length = len(s1)
        flag1 = 1
        flag2 = 1
        temp1 = 0
        temp2 = 0
        for i in range(length):
            if s1[i] == pattern[0] and flag1:
                cnt1 += s1[i+1:].count(pattern[1])
                temp1 = s1[i+1:].count(pattern[1])
                flag1 = 0
            elif s1[i] == pattern[0] and not flag1:
                cnt1 += temp1
            if s1[i] == pattern[1]:
                temp1 -= 1
        s2 = text + pattern[1]
        cnt2 = 0
        for i in range(length):
            if s2[i] == pattern[0] and flag2:
                cnt2 += s2[i + 1:].count(pattern[1])
                temp2 = s2[i + 1:].count(pattern[1])
                flag2 = 0
            elif s2[i] == pattern[0] and not flag2:
                cnt2 += temp2
            if s2[i] == pattern[1]:
                temp2 -= 1
        return max(cnt1, cnt2)


if __name__ == '__main__':
    text = "zigfj"
    pattern = "ju"
    solution = Solution()
    res = solution.maximumSubsequenceCount(text, pattern)
    print(res)