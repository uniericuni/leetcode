# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        if l1 is None and l2 is None:
            return None
        
        head = ListNode(0)
        node = head
        
        while l1 is not None or l2 is not None:
            
            if node.val >= 10:
                node.val -= 10
                node.next = ListNode(1)
            else:
                node.next = ListNode(0)
            node = node.next
            
            if l1 is not None: node.val += l1.val
            else: l1 = ListNode(0)
            if l2 is not None: node.val += l2.val
            else: l2 = ListNode(0)
                
            l1 = l1.next
            l2 = l2.next
        
        if node.val >= 10:
            node.val -= 10
            node.next = ListNode(1)
            
        return head.next
