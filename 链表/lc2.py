class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        dummy = ListNode(-1)
        l3 = dummy
        carry = 0
        while l1 or l2:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            l3.next = ListNode(carry % 10)
            carry = carry // 10
            l3 = l3.next
        if carry:
            l3.next = ListNode(1)
        return dummy.next

l1 = ListNode(9)
l1.next = ListNode(9)
l1.next.next = ListNode(9)
l2 = ListNode(9)
l2.next = ListNode(9)
# l2.next.next = ListNode(9)

solution = Solution()
cur_node = solution.addTwoNumbers(l1, l2)
while cur_node is not None:
    print(cur_node.val)
    cur_node = cur_node.next
