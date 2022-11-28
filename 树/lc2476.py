# Definition for a binary tree node.
import bisect
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        vals = []
        q = [root]
        while q:
            cur = []
            for node in q:
                vals.append(node.val)
                if node.left:
                    cur.append(node.left)
                if node.right:
                    cur.append(node.right)
            q = cur
        ans = []
        vals.sort()
        for query in queries:
            i = bisect.bisect_left(vals, query)
            if i == 0:
                if vals[0] == query:
                    t = [query, query]
                else:
                    t = [-1, vals[0]]
            elif i >= len(vals):
                if vals[-1] == query:
                    t = [query, query]
                else:
                    t = [vals[-1], -1]
            else:
                if vals[i] == query:
                    t = [query, query]
                elif vals[i] < query:
                    t = [vals[i], vals[i+1]]
                else:
                    t = [vals[i-1], vals[i]]
            ans.append(t)
        return ans


if __name__ == '__main__':
    vals = [1, 2, 4, 6, 9, 13, 14, 15]
    query = [-5, 2, 5, 16]
    for q in query:
        i = bisect.bisect_left(vals, q)
        j = bisect.bisect_right(vals, q)
        print(i, j)
