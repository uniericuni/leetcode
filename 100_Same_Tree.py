# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        queue1=[]
        queue2=[]
        queue1.append(p)
        queue2.append(q)
        while len(queue1)>0 and len(queue2)>0:
            p=queue1.pop(0)
            q=queue2.pop(0)
            if p==None and q==None:
                continue
            elif p==None or q==None or p.val!=q.val:
                return False
            else:
                queue1.append(p.left)
                queue1.append(p.right)
                queue2.append(q.left)
                queue2.append(q.right)
        return True
            
