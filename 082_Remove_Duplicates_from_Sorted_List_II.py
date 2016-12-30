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
        rtn=ListNode(0)
        rtn.next=head
        prev=rtn
        node=head
        while node!=None:
            if node.next!=None and node.next.val==node.val:
                while node.next!=None and node.val==node.next.val:
                    node=node.next
                prev.next=node.next
            else:
                prev=prev.next
            node=node.next
        return rtn.next
