class Solution:
    def isThree(self, n: int) -> bool:
        return self.get_number_of_div(n) == 3

    def get_number_of_div(self, n):
        res = 0
        for i in range(1, n+1):
            if n%i==0:
                res += 1
        return res

if __name__ == '__main__':
    s = Solution()
    res = s.isThree(4)
    print(res)