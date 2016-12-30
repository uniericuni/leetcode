# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        node=head
        while node!=None:
            prev=node
            while node.next!=None and node.next.val==prev.val:
                node=node.next
            prev.next=node.next
            node=prev.next
        return head
