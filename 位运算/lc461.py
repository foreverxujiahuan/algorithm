class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x = bin(x)
        y = bin(y)
        x, y = x[2:], y[2:]
        if len(x) > len(y):
            y = '0' * (len(x) - len(y)) + y
        else:
            x = '0' * (len(y) - len(x)) + x
        res = 0
        for i, j in zip(x, y):
            if i != j:
                res += 1
        return res

if __name__ == '__main__':
    x = 3
    y = 1
    solution = Solution()
    res = solution.hammingDistance(x, y)
    print(res)
