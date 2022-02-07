class Solution:
    def reverseWords(self, s: str) -> str:
        temp = s.strip().split(" ")[::-1]
        temp = [t.replace(" ", "") for t in temp]
        temp = [t for t in temp if len(t) >= 1]
        res = " ".join(temp)
        return res


if __name__ == '__main__':
    s = "a good   example"
    so = Solution()
    res = so.reverseWords(s)
    print(res)
