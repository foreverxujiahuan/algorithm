# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root.right and not root.left:
                # 叶子
                return root.val
            elif root.val == 2:
                # or
                return dfs(root.left) or dfs(root.right)
            else:
                return dfs(root.left) and dfs(root.right)

        if dfs(root) == 1:
            return True
        else:
            return False