class Solution:
    def minSteps(self, s: str, t: str) -> int:
        d1 = dict()
        d2 = dict()
        for c in s:
            if c in d1.keys():
                d1[c] += 1
            else:
                d1[c] = 1
        for c in t:
            if c in d2.keys():
                d2[c] += 1
            else:
                d2[c] = 1
        res = 0
        temp = set()
        for k, v in d1.items():
            if k in d2.keys():
                res += abs(v - d2[k])
                temp.add(k)
            else:
                res += v
        for k, v in d2.items():
            if k not in temp:
                if k in d1.keys():
                    res += abs(v - d1[k])
                else:
                    res += v
        return res


if __name__ == '__main__':
    s = "night"
    t = "thing"
    solution = Solution()
    res = solution.minSteps(s, t)
    print(res)
