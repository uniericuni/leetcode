# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        rtn=[]
        stk=[root]
        while len(stk)>0:
            node=stk.pop()
            if node!=None and node.right==None and node.left==None:
                rtn.append(node.val)
            elif node!=None:
                stk.append(node)
                stk.append(node.right)
                stk.append(node.left)
                node.right=None
                node.left=None
        return rtn
