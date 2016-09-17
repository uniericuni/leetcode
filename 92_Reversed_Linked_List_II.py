# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        
        newHead = ListNode(None)
        newHead.next = head
        lNode = newHead
        
        for num in range(1,m):
            lNode = lNode.next
        
        sNode = lNode.next
        for num in range(m,n):
            node = sNode.next
            sNode.next = node.next
            node.next = lNode.next
            lNode.next = node
        
        if m is 1:
            return lNode.next
        else:
            return newHead.next
