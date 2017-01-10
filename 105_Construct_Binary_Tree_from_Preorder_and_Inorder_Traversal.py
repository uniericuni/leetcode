# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def build(self, preorder, inorder):
        if len(inorder)==0:
            return None
            
        curVal=preorder.pop(0)
        curNode=TreeNode(curVal)
        for i,val in enumerate(inorder):
            if val==curVal:
                curNode.left=self.build(preorder, inorder[:i])
                curNode.right=self.build(preorder, inorder[i+1:])
        return curNode
                
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        return self.build(preorder, inorder)    
