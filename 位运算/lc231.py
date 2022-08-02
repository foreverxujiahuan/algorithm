class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        for i in range(-31, 32):
            if 2 ** i == n:
                return True
        return False

if __name__ == '__main__':
    solution = Solution()
    n = 5
    res = solution.isPowerOfTwo(n)
    print(res)
