from collections import deque
from typing import Optional


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        if not root:
            return root
        queue = deque([root])
        while queue:
            length = len(queue)
            for i in range(length - 1):
                queue[i].next = queue[i+1]
            queue[-1].next = None
            new_queue = []
            for q in queue:
                if q.left:
                    l = q.left
                    new_queue.append(l)
                if q.right:
                    r = q.right
                    new_queue.append(r)
            queue = new_queue
        return root
