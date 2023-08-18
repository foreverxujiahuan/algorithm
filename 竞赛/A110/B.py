class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        tmp_nums = []
        length = len(nums)
        for i in range(length):
            tmp_nums.append(nums[i])
            if i != length - 1:
                t = self.hcf(nums[i], nums[i+1])
                tmp_nums.append(t)
        dummy = ListNode(-1)
        l3 = dummy
        for n in tmp_nums:
            l3.next = ListNode(n)
            l3 = l3.next
        return dummy.next

    def hcf(self, p, q):
        tmp = p % q
        while tmp != 0:
            p = q
            q = tmp
            tmp = p % q
        return q

if __name__ == '__main__':
    solution = Solution()
    head = ListNode(1)
    res = solution.insertGreatestCommonDivisors()