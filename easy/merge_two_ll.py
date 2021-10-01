# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        cur = head = ListNode(142857)
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        cur.next = l1 or l2
        return head.next


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
    h1 = list_to_ll([1, 3, 5, 7])
    h2 = list_to_ll([1, 3, 5, 6, 7])
    print(ll_to_list(Solution().mergeTwoLists(h1, h2)))
