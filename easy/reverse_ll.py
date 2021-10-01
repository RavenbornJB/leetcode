# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev


def ll_to_list(head):
    lst = [head.val]
    cur = head
    while cur.next:
        lst.append(cur.next.val)
        cur = cur.next
    return lst


def list_to_ll(lst):
    head = ListNode(val = lst[0])
    cur = head
    for i in range(1, len(lst)):
        node = ListNode(val = lst[i])
        cur.next = node
        cur = node
    return head


if __name__ == '__main__':
    h = list_to_ll([])
    print(ll_to_list(Solution().reverseList(h)))
