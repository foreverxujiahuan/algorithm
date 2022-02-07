class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        for n in range(100000):
            if 2*n*(n+1)*(2*n+1) >= neededApples:
                return n*8
        return 0

if __name__ == '__main__':
    neededApples = 10 ** 15
    s = Solution()
    res = s.minimumPerimeter(neededApples)
    print(res)