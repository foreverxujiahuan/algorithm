# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        root.val = 0
        q = [root]
        while q.count(None) != len(q):
            cur = []
            for node in q:
                if node:
                    cur.append(node.left)
                    cur.append(node.right)
                else:
                    cur.append(None)
                    cur.append(None)
            new_values = []
            s = sum([node.val for node in cur if node])
            length = len(q)
            for i in range(length):
                cur_s = s
                if cur[i * 2]:
                    cur_s -= cur[i * 2].val
                if cur[i * 2 + 1]:
                    cur_s -= cur[i * 2 + 1].val
                if cur[i * 2]:
                    cur[i * 2].val = cur_s
                if cur[i * 2 + 1]:
                    cur[i * 2 + 1].val = cur_s
            q = cur
        return root