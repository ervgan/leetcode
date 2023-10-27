# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# O(N log k) and O(k), 74ms runtime
import heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []
        n = len(lists)
        head = ListNode(None)
        res = head

        for i in range(n):
            node = lists[i]
            if node:
                heapq.heappush(heap, [node.val, i, node])

        while heap:
            node = heappop(heap)
            res.next = node[2]
            res = res.next
            if node[2].next:
                next = node[2].next
                heapq.heappush(heap, [next.val, node[1], next])

        return head.next


# also O(n log k), o(k) 78ms runtime
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists or len(lists) == 0:
            return None


        while len(lists) > 1:
            mergedLists = []

            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i+1] if i+1 < len(lists) else None
                mergedLists.append(self.mergeLists(list1, list2))

            lists = mergedLists

        return lists[0]

    def mergeLists(self, l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                tail = tail.next
                l1 = l1.next
            else:
                tail.next = l2
                tail = tail.next
                l2 = l2.next

        if l1:
            tail.next = l1
            tail = tail.next
        if l2:
            tail.next = l2
            tail = tail.next

        return dummy.next
