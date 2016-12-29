# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        rtn=ListNode(float('inf'))
        node=head
        head=rtn
        while node!=None:
            temp=node.next
            node.next=None
            while head.next!=None and node.val>=head.next.val:
                head=head.next
            node.next=head.next
            head.next=node
            head=rtn
            node=temp
        return rtn.next
