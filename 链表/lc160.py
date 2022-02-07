class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        cur_a = headA
        cur_b = headB
        hash_map = set()
        while cur_a is not None:
            hash_map.add(cur_a)
            cur_a = cur_a.next
        while cur_b is not None:
            if cur_b in hash_map:
                return cur_b
            cur_b = cur_b.next
        return None
