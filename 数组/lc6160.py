from typing import List


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        answers = []
        for q in queries:
            t = self.f(nums, q)
            answers.append(t)
        return answers

    def f(self, arr, n):
        length = len(arr)
        ans = 0
        for i in range(length):
            for j in range(i+1, length):
                if arr[i] + arr[j] <= n and j-i+1 > ans:
                    ans = j-i+1
        return ans

if __name__ == '__main__':
    nums = [4,5,2,1]
    queries = [3,10,21]
    solution = Solution()
    res = solution.answerQueries(nums, queries)
    print(res)