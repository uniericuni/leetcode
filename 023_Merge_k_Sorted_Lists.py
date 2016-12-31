# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def merge(self, head1, head2):
        rtn=ListNode(0)
        node=rtn
        while head1!=None and head2!=None:
            if head1.val>head2.val:
                node.next=head2
                head2=head2.next
            else:
                node.next=head1
                head1=head1.next
            node=node.next
        if head1!=None:
            node.next=head1
        else:
            node.next=head2
        return rtn.next
        
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists)==0:
            return None
        head=lists[0]
        while len(lists)>1:
            head1=lists.pop(0)
            head2=lists.pop(0)
            head=self.merge(head1,head2)
            lists.append(head)
        return head
