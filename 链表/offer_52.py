class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        hash_set = set()
        while headA:
            hash_set.add(headA)
            headA = headA.next
        while headB:
            if headB in hash_set:
                return headB
            headB = headB.next
        return None
