# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur = head = ListNode(0)

        remainder = 0
        while l1 and l2:
            remainder, digit = divmod(l1.val + l2.val + remainder, 10)
            cur.next = ListNode(digit)
            cur = cur.next
            l1, l2 = l1.next, l2.next

        cur.next = l1 or l2
        while cur.next and remainder:
            cur = cur.next
            remainder, cur.val = divmod(cur.val + remainder, 10)

        if remainder:
            cur.next = ListNode(1)
        return head.next


if __name__ == '__main__':
    h1 = ListNode(1)
    h1.next = ListNode(2)
    h1.next.next = ListNode(4)
    h2 = ListNode(4)
    h2.next = ListNode(5)
    h2.next.next = ListNode(6)
    # h2.next.next.next = ListNode(9)
    # 342 + 465 = 807
    res = Solution().addTwoNumbers(h1, h2)

    while res:
        print(res.val)
        res = res.next
