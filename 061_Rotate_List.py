# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head==None:
            return head
        n=0
        node=head
        while node!=None:
            prev=node
            node=node.next
            n+=1
        prev.next=head
        m=n-k%n
        for i in range(0,m):
            prev=head
            head=head.next
        prev.next=None
        return head
