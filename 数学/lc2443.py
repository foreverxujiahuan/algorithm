class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        for i in range(num+1):
            if i + int(str(i)[::-1]) == num:
                return True
        return False

if __name__ == '__main__':
    solution = Solution()
    res = solution.sumOfNumberAndReverse(num=443)
    print(res)