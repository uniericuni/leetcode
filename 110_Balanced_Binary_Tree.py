# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def balance(self, root):
        if root==None:
            return True, 0
        lRtn,lHeight=self.balance(root.left)
        rRtn,rHeight=self.balance(root.right)
        if (not lRtn) or (not rRtn):
            return False, 0
        else:
            return abs(lHeight-rHeight)<=1, max(lHeight, rHeight)+1
        
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        rtn,_=self.balance(root)
        return rtn
