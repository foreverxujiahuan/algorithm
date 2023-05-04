from collections import Counter


class Solution:
    def addMinimum(self, word: str) -> int:
        n_abc = word.count("abc")
        n_ac = word.count("ac")
        n_bc = word.count("bc")
        n_ab = word.count("ab")
        n_a = word.count("a")
        n_b = word.count("b")
        n_c = word.count("c")
        ans = n_ac + (n_bc - n_abc) \
              + (n_ab - n_abc) \
              + 2 * max(0, (n_a - n_ab - n_ac)) \
              + 2 * max(0, (n_b - n_bc - n_ab + n_abc)) \
              + 2 * max(0, (n_c - n_bc - n_ac))
        return ans


if __name__ == '__main__':
    word = "aaabcb"
    solution = Solution()
    res = solution.addMinimum(word)
    print(res)