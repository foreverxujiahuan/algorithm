# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        cur = ListNode(0)
        res = cur
        for n in arr[::-1]:
            cur.next = ListNode(n)
            cur = cur.next
        return res.next
