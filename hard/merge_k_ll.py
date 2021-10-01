import heapq


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        ListNode.__lt__ = lambda self, other: self.val < other.val

        cur = head = ListNode(-69)
        lists = [node for node in lists if node]
        heapq.heapify(lists)

        while lists:
            node = heapq.heappop(lists)
            cur.next = node
            cur = cur.next
            if node.next:
                heapq.heappush(lists, node.next)

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
    h3 = list_to_ll([4])
    print(ll_to_list(Solution().mergeKLists([h1, h2, h3])))
