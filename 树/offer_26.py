class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if B is None or A is None:
            return False
        return self.compare(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)

    def compare(self, A, B):
        if B is None:
            return True
        if A is None:
            return False
        return self.compare(A.left, B.left) and self.compare(A.right, B.right) and A.val == B.val
