# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        rtn=0
        accumulate=0
        stk=[(root,accumulate)]
        while len(stk)!=0:
            node,accumulate=stk.pop()
            if node!=None:
                accumulate=accumulate*10+node.val
                if node.right==None and node.left==None:
                    rtn+=accumulate
                else:
                    stk.append((node.left,accumulate))
                    stk.append((node.right,accumulate))
        return rtn
