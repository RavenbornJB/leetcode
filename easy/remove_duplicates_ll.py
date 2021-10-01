# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur and cur.next:
            if cur.next.val == cur.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head


def ll_to_list(head):
    if not head:
        return []

    lst = [head.val]
    cur = head
    while cur.next:
        lst.append(cur.next.val)
        cur = cur.next
    return lst


if __name__ == '__main__':
    h = ListNode(1)
    h.next = ListNode(2)
    h.next.next = ListNode(2)
    h.next.next.next = ListNode(3)
    h1 = h.next.next.next.next = ListNode(3)
    h1.next = ListNode(4)
    print(ll_to_list(Solution().deleteDuplicates(h)))
