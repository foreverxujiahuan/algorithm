from typing import List


class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        ans = 0
        for word in words:
            if self.f(word, s):
                ans += 1
        return ans

    def f(self, s1, s2):
        parse1 = self.parse(s1)
        parse2 = self.parse(s2)
        if len(parse1) != len(parse2):
            return False
        for (ch1, n1), (ch2, n2) in zip(parse1, parse2):
            if ch1 != ch2:
                return False
            if n2 < n1 or (n2 < 3 and n2 != n1):
                return False
        return True

    def parse(self, s):
        res = []
        length = len(s)
        i = 0
        cur_n = 0
        cur_s = ''
        while i < length:
            if not cur_s:
                cur_s = s[i]
                cur_n += 1
            else:
                if s[i] == cur_s:
                    cur_n += 1
                else:
                    res.append((cur_s, cur_n))
                    cur_s = s[i]
                    cur_n = 1
            i += 1
        res.append((cur_s, cur_n))
        return res


if __name__ == '__main__':
    # s = "dddiiiinnssssssoooo"
    # words = ["dinnssoo", "ddinso", "ddiinnso", "ddiinnssoo", "ddiinso", "dinsoo", "ddiinsso", "dinssoo", "dinso"]
    s = "heeellooo"
    words = ["hello", "hi", "helo"]
    solution = Solution()
    res = solution.expressiveWords(s, words)
    print(res)
