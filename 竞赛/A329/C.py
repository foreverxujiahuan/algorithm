class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        tmp = ""
        for c1, c2 in zip(s, target):
            if c1 != c2:
                tmp += c1
        cnt1 = tmp.count('1')
        cnt0 = tmp.count('0')
        if cnt1 >= cnt0 != 0:
            return True
        return False


if __name__ == '__main__':
    s = "100101000101110001"
    target = "000101000000110001"
    solution = Solution()
    res = solution.makeStringsEqual(s, target)
    print(res)