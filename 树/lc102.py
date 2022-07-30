from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        ans = []
        while queue:
            t = [node.val for node in queue]
            ans.append(t)
            cur_queue = []
            for node in queue:
                if node.left:
                    cur_queue.append(node.left)
                if node.right:
                    cur_queue.append(node.right)
            queue = cur_queue
        return ans
