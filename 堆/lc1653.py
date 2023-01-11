class Solution:
    def minimumDeletions(self, s: str) -> int:
        stack = []
        for c in s:
            if c == 'b':
                stack.append(c)
        return 0
