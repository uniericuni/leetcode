# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head==None:
            return head
        s=ListNode(0)
        l=ListNode(0)
        sHead=s
        lHead=l
        while head!=None:
            if head.val<x:
                s.next=head
                s=s.next
            else:
                l.next=head
                l=l.next
            head=head.next
        l.next=None
        s.next=lHead.next
        return sHead.next
