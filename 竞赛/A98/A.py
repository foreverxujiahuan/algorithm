class Solution:
    def minMaxDifference(self, num: int) -> int:
        candidate = []
        s = "0123456789"
        for c1 in s:
            for c2 in s:
                cur = str(num).replace(c1, c2)
                candidate.append(int(cur))
        return max(candidate) - min(candidate)



if __name__ == '__main__':
    num = 90
    solution = Solution()
    res = solution.minMaxDifference(num)
    print(res)
