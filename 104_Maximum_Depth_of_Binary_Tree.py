# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMax(self, node, rtn, maxV):
        if node==None:
            return max(rtn, maxV)
        else:
            r=self.findMax(node.right, rtn+1, maxV)
            l=self.findMax(node.left, rtn+1, maxV)
            return max(r,l)
            
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        rtn=0
        maxV=0
        return self.findMax(root, rtn, maxV)
