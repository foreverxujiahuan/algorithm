from typing import List


class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        ans = []
        for query in queries:
            for d in dictionary:
                if self.f(query, d) <= 2:
                    ans.append(query)
                    break
        return ans

    def f(self, s1, s2):
        if len(s1) != len(s2):
            return 3
        ans = 0
        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                ans += 1
        return ans

if __name__ == '__main__':
    # queries = ["word", "note", "ants", "wood"]
    # dictionary = ["wood", "joke", "moat"]
    queries = ["yes"]
    dictionary = ["not"]
    solution = Solution()
    res = solution.twoEditWords(queries, dictionary)
    print(res)