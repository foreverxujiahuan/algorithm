class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        res = 0
        while n != 0:
            n = n // 2
            res += 1
            if res >= k:
                res += n
                return res
        return res


if __name__ == '__main__':
    solution = Solution()
    res = solution.superEggDrop(1, 3)
    print(res)