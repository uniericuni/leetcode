# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev=ListNode(0)
        rtn=prev
        prev.next=head
        node=head
        while node!=None and node.next!=None:
            prev.next=node.next
            node.next=node.next.next
            prev.next.next=node
            prev=node
            node=node.next
        return rtn.next
