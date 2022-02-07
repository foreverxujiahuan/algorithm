import sys


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.dfs(root, -sys.maxsize-1, sys.maxsize)

    def dfs(self, root, min_value, max_value):
        if root is None:
            return True
        if root.val <= min_value or root.val >= max_value:
            return False
        return self.dfs(root.left, min_value, root.val) and self.dfs(root.right, root.val, max_value)

