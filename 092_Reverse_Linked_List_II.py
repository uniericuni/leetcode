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
        rtn=ListNode(0)
        rtn.next=head
        prev=rtn
        node=head
        for i in range(1,m):
            node=node.next
            prev=prev.next
        head=prev
        tail=node
        for i in range(m,n):
            node=head.next
            head.next=tail.next
            tail.next=tail.next.next
            head.next.next=node
            
        return rtn.next
