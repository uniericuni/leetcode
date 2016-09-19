# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        if root is None:
            return []
        
        waitStack = []
        rList = []
        node = root
        waitStack.append(node)
        
        while len(waitStack) is not 0:
            node = waitStack[len(waitStack)-1]
            waitStack.pop()
            if node.left is None and node.right is None:
                rList.append(node.val)
                continue
            if node.right is not None:
                waitStack.append(node.right)
                node.right = None
            waitStack.append(node)
            if node.left is not None:
                waitStack.append(node.left)
                node.left = None
                
        return rList
