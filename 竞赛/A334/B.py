from typing import List


class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        ans, x = [], 0
        for c in word:
            d = int(c)
            x = (x * 10 + d) % m
            ans.append(int(x == 0))
        return ans


if __name__ == '__main__':
    word = "998244353"
    m = 3
    solution = Solution()
    res = solution.divisibilityArray(word, m)
    print(res)
