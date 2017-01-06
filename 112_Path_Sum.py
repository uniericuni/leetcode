# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        s=0
        stk=[(root,s)]
        while len(stk)!=0:
            node,s=stk.pop()
            if node!=None:
                print s
                s+=node.val
                if node.right==None and node.left==None:
                    if s==sum:  return True
                stk.append((node.right,s))
                stk.append((node.left,s))
        return False
