# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return False
        
        turtle = head
        rabbit = head
        while rabbit != None:
            if rabbit.next == None: return False
            turtle = turtle.next
            rabbit = rabbit.next.next
            if turtle == rabbit: return True
        return False
