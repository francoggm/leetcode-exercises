from typing import Optional
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current, len = head, 0
        while current:
            current, len = current.next, len + 1
        middle = len // 2
        for _ in range(middle):
            head = head.next
        return head


if __name__ == '__main__':
    head = ListNode(5)
    head.next = ListNode(7)

