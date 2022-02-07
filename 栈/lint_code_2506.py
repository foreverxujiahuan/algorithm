class Solution:
    """
    @param s: A string with lowercase letters and parentheses
    @return: A string which has been removed invalid parentheses
    """
    def removeParentheses(self, s: str) -> str:
        # write your code here.
        stack = []
        res = []
        for c in s:
            if c == '(':
                stack.append(c)
                res.append(c)
            elif c == ')' and stack[-1] == '(':
                pass
            else:
                pass
        return "".join(res)