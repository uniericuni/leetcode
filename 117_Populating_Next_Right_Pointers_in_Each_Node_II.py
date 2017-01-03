# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        stk=[root]
        while len(stk)>0:
            stkTemp=[]
            prev=None
            while len(stk)>0:
                node=stk.pop()
                if node!=None:
                    node.next=prev
                    prev=node
                    stkTemp.insert(0,node.right)
                    stkTemp.insert(0,node.left)
            stk=stkTemp
