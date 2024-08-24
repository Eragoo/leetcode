# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)

        l1c = list1
        l2c = list2
        cur = dummy
        while l1c and l2c:
            if l1c.val < l2c.val:
                cur.next = l1c
                l1c = l1c.next
            else:
                cur.next = l2c
                l2c = l2c.next
            cur = cur.next

        if l1c:
            cur.next = l1c
        if l2c:
            cur.next = l2c
        return dummy.next