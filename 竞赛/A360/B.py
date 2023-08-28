class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        s = 0
        cur_set = set()
        i = 1
        while len(cur_set) != n:
            if target - i not in cur_set and i not in cur_set:
                s += i
                cur_set.add(i)
            else:
                i += 1
        return s


if __name__ == '__main__':
    n = 16
    target = 6
    solution = Solution()
    res = solution.minimumPossibleSum(n, target)
    print(res)