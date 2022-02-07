from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        output = []
        cur = [root]
        while cur:
            temp = []
            for node in cur:
                if not node:
                    continue
                output.append(node.val)
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            cur = temp
        return output
