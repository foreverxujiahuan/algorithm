


class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        s1_0 = []
        s1_1 = []
        s2_0 = []
        s2_1 = []
        for i, (c1, c2) in enumerate(zip(s1, s2)):
            if i % 2 == 0:
                s1_0.append(c1)
                s2_0.append(c2)
            else:
                s1_1.append(c1)
                s2_1.append(c2)
        if sorted(s1_0) == sorted(s2_0) and sorted(s1_1) == sorted(s2_1):
            return True
        return False


if __name__ == '__main__':
    solution = Solution()
    s1 = "d"
    s2 = "d"
    res = solution.checkStrings(s1, s2)
    print(res)