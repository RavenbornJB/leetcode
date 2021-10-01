# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        reverse = None
        slow = fast = head

        while fast and fast.next:
            tmp = reverse
            reverse = slow
            slow = slow.next
            fast = fast.next.next
            reverse.next = tmp

        if fast:
            slow = slow.next

        while reverse and reverse.val == slow.val:
            reverse, slow = reverse.next, slow.next

        return not slow


if __name__ == '__main__':
    h = ListNode(4)
    h.next = ListNode(5)
    h.next.next = ListNode(5)
    h.next.next.next = ListNode(4)
    # h.next.next.next.next = ListNode(1)
    print(Solution().isPalindrome(h))
