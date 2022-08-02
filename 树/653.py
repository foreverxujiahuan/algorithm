from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        nums = []
        queue = [root]
        while queue:
            t = [node.val for node in queue]
            nums.extend(t)
            cur_queue = []
            for node in queue:
                if node.left:
                    cur_queue.append(node.left)
                if node.right:
                    cur_queue.append(node.right)
            queue = cur_queue
        nums = list(set(nums))
        nums.sort()
        length = len(nums)
        for i in range(length):
            for j in range(i+1, length):
                if nums[i] + nums[j] == k:
                    return True
        return False
