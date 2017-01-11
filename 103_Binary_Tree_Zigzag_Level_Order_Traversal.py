# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzag(self, stk, rtn, flag):
        tempRtn=[]
        tempStk=[]
        if flag:
            while len(stk)!=0:
                node=stk.pop()
                if node!=None:
                    tempRtn.append(node.val)
                    tempStk.append(node.left)
                    tempStk.append(node.right)
        else:
            while len(stk)!=0:
                node=stk.pop()
                if node!=None:
                    tempRtn.append(node.val)
                    tempStk.append(node.right)
                    tempStk.append(node.left)
        if len(tempRtn)==0:
            return rtn
        rtn.append(tempRtn)
        flag=not flag
        return self.zigzag(tempStk, rtn, flag)
        
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        rtn=[]
        self.zigzag([root], rtn, True)
        return rtn
