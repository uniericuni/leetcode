# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMin(self, node, rtn, minV):
        if node!=None:
            if node.right==None and node.left==None:
                return min(rtn+1, minV)
            if node.right!=None:
                r=self.findMin(node.right, rtn+1, minV)
                minV=min(r,minV)
            if node.left!=None:
                l=self.findMin(node.left, rtn+1, minV)
                minV=min(l,minV)
            return minV
        else:
            return 0
            
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        rtn=0
        minV=float('inf')
        return self.findMin(root, rtn, minV)
