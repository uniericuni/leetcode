# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        node1 = head
        node2 = head
        prev = ListNode(float('inf'))
        prev.next = head
        for n in range(0,n-1):
            node1 = node1.next
        while node1.next != None:
            prev = node2
            node1 = node1.next
            node2 = node2.next
        if prev.next == head:
            prev.next = node2.next
            return prev.next
        else:
            prev.next = node2.next
            return head
