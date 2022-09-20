from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = [root]
        flag = 0
        while queue[0].left:
            new_queue = []
            for node in queue:
                new_queue.append(node.left)
                new_queue.append(node.right)
            queue = new_queue
            length = len(queue)
            if flag == 0:
                for i in range(length // 2):
                    x, y = queue[i].val, queue[length - i - 1].val
                    queue[i].val, queue[length - i - 1].val = y, x
            flag ^= 1
        return root

