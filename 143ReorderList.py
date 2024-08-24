# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        cache = []

        cur = head
        while cur:
            cache.append(cur)
            cur = cur.next

        l, r = 1, len(cache) - 1

        cur = head
        res = cur
        while l < r:
            cur.next = cache[r]
            cur.next.next = cache[l]
            l += 1
            r -= 1

            cur = cur.next.next

        cur.next = None
        return res