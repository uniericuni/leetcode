# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValid(self, node):
        if node==None:
            return 0
        rtn1 = self.isValid(node.left)
        rtn2 = self.isValid(node.right)
        if rtn1==-1 or rtn2==-1 or abs(rtn1-rtn2)>1:
            return -1
        else:
            return max(rtn1,rtn2)+1
    
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        rtn = self.isValid(root)
        if rtn==-1:
            return False
        return True
        
        
