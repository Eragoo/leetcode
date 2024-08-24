# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cache = {}
        if not head:
            return head

        cur = head
        while cur:
            cache[cur] = Node(cur.val, None, None)
            cur = cur.next

        cur = head
        first = cache[cur]
        while cur:
            current = cache[cur]
            if cur.next:
                current.next = cache[cur.next]
            if cur.random:
                current.random = cache[cur.random]

            cur = cur.next

        return first


if __name__ == '__main__':
    print(Solution().copyRandomList(Node(1, Node(2, None))))