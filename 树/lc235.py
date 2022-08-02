# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def get_path(root, target):
            path = []
            node = root
            while node != target:
                path.append(node)
                if node.val > target.val:
                    node = node.left
                else:
                    node = node.right
            path.append(node)
            return path

        path1 = get_path(root, p)
        path2 = get_path(root, q)
        ans = None
        for i, j in zip(path1, path2):
            if i == j:
                ans = i
            else:
                break
        return ans
