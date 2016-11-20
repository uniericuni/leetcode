# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):  
        """
        :type head: ListNode
        :rtype: bool
        """
        turtle = head
        rabbit = head
        while rabbit!=None and rabbit.next!=None:
            turtle = turtle.next
            rabbit = rabbit.next.next
            if turtle == rabbit:
                turtle = head
                while rabbit!=turtle:
                    turtle = turtle.next
                    rabbit = rabbit.next
                return rabbit
        return 
