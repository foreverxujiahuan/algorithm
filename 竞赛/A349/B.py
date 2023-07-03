from string import ascii_lowercase
from torchtext.data.utils import get_tokenizer

class Solution:
    def smallestString(self, s: str) -> str:
        d = dict()
        for i, c in enumerate(ascii_lowercase):
            d[c] = ascii_lowercase[i-1]
        a_cnt = 0
        for i, c in enumerate(s):
            if c == 'a':
                a_cnt += 1
            else:
                break
        s = s[a_cnt: ]
        if 'a' in s:
            index = s.index("a")
        else:
            index = len(s)
        cur = s[:index]
        tmp1 = ""
        if cur:
            tmp1 = ""
            for c in cur:
                tmp1 += d[c]
        tmp2 = s[index:]
        ans = 'a' * a_cnt + tmp1 + tmp2
        return ans

if __name__ == '__main__':
    solution = Solution()
    s = "baabc"
    res = solution.smallestString(s)
    print(res)