
class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans = 0
        for i in range(low, high+1):
            s = str(i)
            if len(s) % 2 != 0:
                continue
            mid = len(s) // 2
            if sum([int(i) for i in s[:mid]])  == sum([int(i) for i in s[mid:]]):
                ans +=1
        return ans


if __name__ == '__main__':
    solution = Solution()
    low = 1
    high = 100
    res = solution.countSymmetricIntegers(low, high)
    print(res)