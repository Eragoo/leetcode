# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l, r = None, head

        while r:
            next = r.next

            r.next = l
            l = r
            r = next
        return l




if __name__ == '__main__':
    print(Solution().reverseList(
        ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))))