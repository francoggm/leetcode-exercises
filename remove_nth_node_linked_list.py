from typing import Optional

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current, nth = head, 0
        while current:
            if n == nth + 1:
                current.next = current.next.next
            current, nth = current.next, nth + 1
        return head