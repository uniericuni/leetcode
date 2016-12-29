# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverse(self, head):
        if head==None:
            return head
        rtn=ListNode(0)
        rtn.next=head
        node=head
        while head.next!=None:
            rtn.next=head.next
            head.next=head.next.next
            rtn.next.next=node
            node=rtn.next
        return rtn.next
        
    def merge(self, head1, head2):
        node=ListNode(0)
        while head1!=None and head2!=None:
            node.next=head1
            head1=head1.next
            node.next.next=head2
            head2=head2.next
            node=node.next.next
        if head1!=None:
            node.next=head1
        else:
            node.next=head2
        
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head==None:
            return head
        slow=head
        fast=head.next
        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
        fast=slow.next
        slow.next=None
        fast=self.reverse(fast)
        self.merge(head,fast)
