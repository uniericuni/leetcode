# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.rtn = 0
        self.bfs(root, sum)
        return self.rtn
        
    def bfs(self, node, sum):
        if node==None:
            return
        self.dfs(node, sum)
        self.bfs(node.left, sum)
        self.bfs(node.right, sum)
        
    def dfs(self, node, sum):
        if node==None:
            return
        if node.val == sum:
            self.rtn += 1
        self.dfs(node.left, sum-node.val)
        self.dfs(node.right, sum-node.val)
