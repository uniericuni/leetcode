# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        rtn=[]
        stk=[]
        stk.append(root)
        node=root
        while len(stk)>0:
            if node==None:
                node=stk.pop()
            else:
                rtn.append(node.val)
                stk.append(node.right)
                node=node.left
                
        return rtn
