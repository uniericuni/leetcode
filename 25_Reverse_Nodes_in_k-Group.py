# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        n = 0
        node = head
        while node is not None:
            node = node.next
            n += 1
            
        r = n%k
        q = n/k
        preHead = ListNode(0)
        nodeHead = preHead
        node = head
        headFlag = 0
        for i in range(0,q):
            prev = nodeHead
            preHead = nodeHead
            nodeHead = node
            for j in range(0,k):
                preHead.next = node
                nodeHead.next = node.next
                if j is not 0:
                    node.next = prev
                prev = node
                node = nodeHead.next
            if headFlag is 0:
                head = prev
                headFlag = 1
                
        return head
