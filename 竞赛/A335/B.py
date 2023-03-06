# Definition for a binary tree node.
from heapq import nlargest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        q = [root]
        candidates = []
        while q:
            cur_s = 0
            new_q = []
            for node in q:
                if node:
                    cur_s += node.val
                if node.left:
                    new_q.append(node.left)
                if node.right:
                    new_q.append(node.right)
            q = new_q
            candidates.append(cur_s)
        if k > len(candidates):
            return -1
        return sorted(candidates, reverse=True)[k-1]
