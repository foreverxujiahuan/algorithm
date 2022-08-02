from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = [[]]

        for char in s:
            n = len(ans)
            if char.isalpha():
                for i in range(n):
                    ans.append(ans[i][:])
                    ans[i].append(char.lower())
                    ans[n+i].append(char.upper())
            else:
                for i in range(n):
                    ans[i].append(char)

        return ["".join(t) for t in ans]

if __name__ == '__main__':
    s = "a1b2"
    solution = Solution()
    res = solution.letterCasePermutation(s)
    print(res)