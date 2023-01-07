from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length = len(temperatures)
        ans = [0] * length
        stack = []
        for i in range(length):
            temperature = temperatures[i]
            while stack and temperature > temperatures[stack[-1]]:
                prev_index = stack.pop()
                ans[prev_index] = i - prev_index
            stack.append(i)
        return ans


if __name__ == '__main__':
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    solution = Solution()
    res = solution.dailyTemperatures(temperatures)
    print(res)

