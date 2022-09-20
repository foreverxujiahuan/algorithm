class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        queue = [root]
        index = 0
        while queue:
            length = len(queue)
            nums = []
            for i in range(length):
                cur = queue[i]
                if cur.left:
                    nums.append(cur.left.val)
                if cur.right:
                    nums.append(cur.right.val)
            if index % 2 != 0:
                for i in range(length):
                    cur_node = queue.pop(0)
                    if cur_node.left:
                        queue.append(cur_node.left)
                    if cur_node.right:
                        queue.append(cur_node.right)
            else:
                for i in range(length):
                    cur_node = queue.pop(0)
                    if cur_node.left:
                        queue.append(cur_node.left)
                    if cur_node.right:
                        queue.append(cur_node.right)
        return root

