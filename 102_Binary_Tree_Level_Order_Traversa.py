# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        q=[root]
        rtn=[]
        while len(q)!=0:
            rtnTemp=[]
            qTemp=[]
            while len(q)!=0:
                node=q.pop(0)
                if node!=None:
                    rtnTemp.append(node.val)
                    qTemp.append(node.left)
                    qTemp.append(node.right)
            q=qTemp
            if len(rtnTemp)!=0:
                rtn.append(rtnTemp)
            
        return rtn
