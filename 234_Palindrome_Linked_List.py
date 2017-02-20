# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        if head==None: return True
        
        node = head
        n = 0
        while node!=None:
            node = node.next
            n += 1
        mid = n/2

        node = head
        prev = None
        for i in range(mid):
            tmp = node.next
            node.next = prev
            prev = node
            node = tmp
        
        node1 = prev
        node2 = node
        if n%2==1: node2 = node2.next
        while node1!=None:
            if node1.val!=node2.val:
                return False
            node1 = node1.next
            node2 = node2.next
            
        return True
