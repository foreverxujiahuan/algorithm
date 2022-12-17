from collections import Counter


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        counter = Counter(s)
        for c in s:
            if c not in stack:
                while stack and c < stack[-1] and counter[stack[-1]] > 0:
                    stack.pop()
                stack.append(c)
            counter[c] -= 1
        return "".join(stack)


if __name__ == '__main__':
    solution = Solution()
    s = "cbacdcbc"
    res = solution.removeDuplicateLetters(s)
    print(res)
