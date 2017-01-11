# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root==None:
            return True
        lQ=[root.left]
        rQ=[root.right]
        while len(lQ)!=0 and len(rQ)!=0:
            tempLQ=[]
            tempRQ=[]
            while len(lQ)!=0 and len(rQ)!=0:
                l=lQ.pop()
                r=rQ.pop()
                if l==None and r==None: continue
                if l==None or r==None or l.val!=r.val: return False
                if l!=None:
                    tempLQ.append(l.right)
                    tempLQ.append(l.left)
                    tempRQ.append(r.left)
                    tempRQ.append(r.right)
            lQ=tempLQ
            rQ=tempRQ
        return True
