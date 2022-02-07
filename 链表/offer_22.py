class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        temp = head
        length = 0
        while temp:
            temp = temp.next
            length += 1

        for i in range(length - k):
            head = head.next

        return head
