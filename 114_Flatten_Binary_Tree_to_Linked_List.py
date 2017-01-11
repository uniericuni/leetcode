# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        stk=[]
        node=root
        while node!=None:
            l=node.left
            node.left=None
            r=node.right
            if r!=None:
                stk.append(r)
            if l!=None:
                node.right=l
            else:
                if len(stk)==0:
                    break
                else:
                    node.right=stk.pop()
            node=node.right
