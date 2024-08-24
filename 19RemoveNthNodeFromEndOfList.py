# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i = 0
        cur = head
        while cur:
            i += 1
            cur = cur.next

        depth = i - n + 1
        dummy = ListNode(-1, head)
        cur = dummy
        i = 1
        while cur:
            if i == depth and cur.next:
                cur.next = cur.next.next
                break
            cur = cur.next
            i += 1

        return dummy.next