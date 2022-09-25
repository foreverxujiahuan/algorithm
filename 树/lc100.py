from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (not p) ^ (not q):
            return False
        if not p and not q:
            return True
        queue1, queue2 = deque([p]), deque([q])
        while queue1 and queue2:
            node1, node2 = queue1.popleft(), queue2.popleft()
            if node1.val != node2.val:
                return False
            if (not node1.left) ^ (not node2.left):
                return False
            if (not node1.right) ^ (not node2.right):
                return False
            if node1.left:
                queue1.append(node1.left)
            if node1.right:
                queue1.append(node1.right)
            if node2.left:
                queue2.append(node2.left)
            if node2.right:
                queue2.append(node2.right)

        return not queue1 and not queue2


