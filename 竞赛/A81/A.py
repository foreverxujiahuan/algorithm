class Solution:
    def countAsterisks(self, s: str) -> int:
        temp = s.split("|")
        res = 0
        for i in range(len(temp)):
            if i % 2 == 0:
                res += temp[i].count("*")
        return res


if __name__ == '__main__':
    solution = Solution()
    s = "yo|uar|e**|b|e***au|tifu|l"
    res = solution.countAsterisks(s)
    print(res)