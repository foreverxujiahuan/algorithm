class Solution:
    def splitNum(self, num: int) -> int:
        s = list(str(num))
        s.sort()
        length = len(s)
        s1 = ""
        s2 = ""
        flag = 1
        for i in range(length):
            if s[i] == '0':
                continue
            if flag == 1:
                s1 += s[i]
            else:
                s2 += s[i]
            flag = flag * -1
        if not s1:
            return int(s2)
        if not s2:
            return int(s1)
        return int(s1) + int(s2)


if __name__ == '__main__':
    num = 10
    solution = Solution()
    res = solution.splitNum(num)
    print(res)





