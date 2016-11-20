# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node = head
        prev_node = None
        while node != None:
            temp = node.next
            node.next = prev_node
            prev_node = node
            node = temp
        return prev_node
