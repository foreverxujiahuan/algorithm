class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        s = ' '.join([x for x in s.split(' ') if len(x) > 0])
        temp = s.split(" ")[::-1]
        return ' '.join(temp)

s = "a good   example"
solution = Solution()
res = solution.reverseWords(s)
print(res)
