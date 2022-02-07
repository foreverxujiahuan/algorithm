class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def hasCycle(self, head: ListNode) -> ListNode:
        hash_map = set()
        cur = head
        while cur is not None:
            if cur in hash_map:
                return cur
            else:
                hash_map.add(cur)
            cur = cur.next
        return None
