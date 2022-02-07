class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        hash_map = set()
        cur = head
        while cur is not None:
            if cur in hash_map:
                return True
            else:
                hash_map.add(cur)
            cur = cur.next
        return False

    def hasCycle2(self, head: ListNode) -> bool:
        slow = head
        fast = head
        while slow is not None and fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
