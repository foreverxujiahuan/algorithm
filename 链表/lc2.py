class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        new_node = ListNode(-1)
        l3 = new_node
        carry = 0
        while l1 is not None or l2 is not None:
            if l1 is not None:
                carry += l1.val
                l1 = l1.next
            if l2 is not None:
                carry += l2.val
                l2 = l2.next
            l3.next = ListNode(carry % 10)
            carry = int(carry/10)
            l3 = l3.next
        if carry == 1:
            l3.next = ListNode(1)
        return new_node.next


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

solution = Solution()
cur_node = solution.addTwoNumbers(l1, l2)
while cur_node is not None:
    print(cur_node.val)
    cur_node = cur_node.next
