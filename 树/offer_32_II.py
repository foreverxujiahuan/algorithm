from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        output = []
        cur = [root]
        while cur:
            temp_val = []
            temp_node = []
            for node in cur:
                if node:
                    temp_val.append(node.val)
                else:
                    continue
                if node.left:
                    temp_node.append(node.left)
                if node.right:
                    temp_node.append(node.right)
            if temp_val:
                output.append(temp_val)
            cur = temp_node
        return output
