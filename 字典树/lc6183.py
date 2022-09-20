from collections import defaultdict
from typing import List


class Node:
    def __init__(self):
        self.son = defaultdict(Node)
        self.ids = []
        self.score = 0


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        root = Node()
        for i, word in enumerate(words):
            cur = root
            for c in word:
                cur = cur.son[c]
                cur.score += 1  # 更新所有前缀的分数
            cur.ids.append(i)

        ans = [0] * len(words)

        def dfs(node: Node, sum: int) -> None:
            sum += node.score  # 累加分数，即可得到答案
            for i in node.ids:
                ans[i] = sum
            for child in node.son.values():
                if child:
                    dfs(child, sum)

        dfs(root, 0)
        return ans


if __name__ == '__main__':
    words = ["abc", "ab", "bc", "b"]
    solution = Solution()
    ans = solution.sumPrefixScores(words)
    print(ans)
