from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start = prev = ListNode(-101)
        start.next = head

        remove = False
        while head:

            if head.next and head.val == head.next.val:
                remove = True
            elif remove:
                remove = False
                prev.next = head.next
            else:
                prev = head
            head = head.next

        return start.next


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
