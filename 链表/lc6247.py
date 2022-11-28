
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        filter_arr = []
        length = len(arr)
        max_values = [0 for _ in range(length)]
        for i in range(length-1, -1, -1):
            if i == length-1:
                max_values[i] = arr[i]
            elif arr[i] <= max_values[i+1]:
                max_values[i] = max_values[i+1]
            else:
                max_values[i] = arr[i]
        for i in range(length-1):
            if arr[i] < max_values[i]:
                continue
            filter_arr.append(arr[i])
        filter_arr.append(arr[-1])
        ans = ListNode(-1)
        cur = ans
        for n in filter_arr:
            cur.next = ListNode(n)
            cur = cur.next
        return ans.next

