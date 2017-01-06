# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSum(self, node, stk, rtn, s, sum):
        if node!=None:
            stk.append(node.val)
            s+=node.val
            if node.right==None and node.left==None and s==sum:
                rtn.append(stk)
            self.findSum(node.left, stk[:], rtn, s, sum)
            self.findSum(node.right, stk[:], rtn, s, sum)

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        s=0
        stk=[]
        rtn=[]
        node=root
        self.findSum(node, stk[:], rtn, s, sum)
        return rtn
