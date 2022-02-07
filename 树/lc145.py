from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        node_list = []
        self.dfs(root, node_list)
        return node_list

    def dfs(self, node, node_list):
        if node is None:
            return
        self.dfs(node.left, node_list)
        self.dfs(node.right, node_list)
        node_list.append(node.val)
