class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        cur = ListNode(0)
        res = cur
        while head:
            if head.val != val:
                cur.next = ListNode(head.val)
                cur = cur.next
            head = head.next
        return res.next