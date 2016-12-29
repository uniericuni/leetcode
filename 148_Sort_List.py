# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def merge(self, head1, head2):
        head=ListNode(0)
        rtn=head
        while head1!=None and head2!=None:
            if head1.val<head2.val:
                head.next=head1
                head=head1
                head1=head1.next
            else:
                head.next=head2
                head=head2
                head2=head2.next
        if head1==None:
            head.next=head2
        else:
            head.next=head1
        return rtn.next
        
    def mergeSort(self, head):
        if head.next==None:
            return head
        slow=head
        fast=head.next
        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
        fast=slow.next
        slow.next=None
        slow=self.mergeSort(head)
        fast=self.mergeSort(fast)
        head=self.merge(slow, fast)
        return head
        
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None:
            return head
        head=self.mergeSort(head)
        return head
