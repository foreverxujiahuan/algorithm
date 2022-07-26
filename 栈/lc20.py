

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []
        for ch in s:
            if ch in "([{":
                stack.append(ch)
            else:
                if not stack:
                    return False
                elif ch == ')' and stack[-1] == '(':
                    stack.pop()
                elif ch == '}' and stack[-1] == '{':
                    stack.pop()
                elif ch == ']' and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
        return len(stack) == 0

if __name__ == '__main__':
    s = ")["
    soltuion = Solution()
    res = soltuion.isValid(s)
    print(res)

