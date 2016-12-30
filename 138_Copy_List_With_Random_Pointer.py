# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        
        if head==None:
            return head
        
        p=RandomListNode(head.label)
        rtn=p
        dict={}
        while head!=None:
            if head.next!=None:
                if head.next in dict:
                    p.next=dict[head.next]
                else:
                    p.next=RandomListNode(head.next.label)
                    dict[head.next]=p.next
            if head.random!=None:
                if head.random in dict:
                    p.random=dict[head.random]
                else:
                    p.random=RandomListNode(head.random.label)
                    dict[head.random]=p.random
            p=p.next
            head=head.next
                
        return rtn
