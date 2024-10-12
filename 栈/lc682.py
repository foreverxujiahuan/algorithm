from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op.isdigit() or op.startswith("-"):
                stack.append(int(op))
            elif op == 'C':
                stack.pop()
            elif op == 'D':
                stack.append(stack[-1] * 2)
            elif op == '+':
                stack.append(stack[-1] + stack[-2])
        return sum(stack)

if __name__ == '__main__':
    solution = Solution()
    ops = ["5","-2","4","C","D","9","+","+"]
    res = solution.calPoints(ops)
    print(res)