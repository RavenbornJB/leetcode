# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def ll_len(self, head):
        cur = head
        size = 1
        while cur.next:
            cur = cur.next
            size += 1
        return size

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lenA, lenB = self.ll_len(headA), self.ll_len(headB)

        curA, curB = headA, headB
        if lenA > lenB:
            for _ in range(lenA - lenB):
                curA = curA.next
        else:
            for _ in range(lenB - lenA):
                curB = curB.next
        while curA is not curB:
            curA = curA.next
            curB = curB.next

        return curA


def ll_to_list(head):
    lst = [head.val]
    cur = head
    while cur.next:
        lst.append(cur.next.val)
        cur = cur.next
    return lst


if __name__ == '__main__':
    h1 = ListNode(4)
    h1.next = ListNode(1)
    h1.next.next = ListNode(8)
    h2 = ListNode(5)
    h2.next = ListNode(6)
    h2.next.next = ListNode(1)
    h2.next.next.next = h1.next.next
    print(ll_to_list(Solution().getIntersectionNode(h1, h2)))
