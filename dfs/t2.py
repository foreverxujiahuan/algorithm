
class Solution:

    def unique_subsequence_sums(self, arr):
        def backtrack(start, path):
            # 将当前路径的和添加到结果中
            if path:
                sums.append(sum(path))
            # 遍历数组中的每个元素
            for i in range(start, len(arr)):
                # 选择当前元素，并递归地选择剩余的元素
                backtrack(i + 1, path + [arr[i]])

        sums = []
        backtrack(0, [])
        return sums


    def getCurrencyNumber(self, n, currencyValue, currencyAmount, x):
        arr = []
        for i, j in zip(currencyValue, currencyAmount):
            arr += [i] * j
        value = self.unique_subsequence_sums(arr)
        value = [v for v in value if v != 0]
        ans = len([v for v in value if v % x == 0])
        return ans

n = 3
currencyValue = [5,3,1]
currencyAmount = [1,1,1]
x = 3
solution = Solution()
ans = solution.getCurrencyNumber(n,currencyValue,currencyAmount,x)
print(ans)
