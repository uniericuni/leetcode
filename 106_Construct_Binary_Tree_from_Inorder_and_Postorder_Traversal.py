# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def build(self, postorder, inorder):
        if len(inorder)==0:
            return None
            
        curVal=postorder.pop()
        curNode=TreeNode(curVal)
        for i,val in enumerate(inorder):
            if val==curVal:
                curNode.right=self.build(postorder, inorder[i+1:])
                curNode.left=self.build(postorder, inorder[:i])
        return curNode
                
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        return self.build(postorder, inorder)    
