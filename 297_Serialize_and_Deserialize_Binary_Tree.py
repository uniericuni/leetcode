# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import re

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        rtn = ''
        return '['+self.debuild([root],rtn,1)[:-1]+']'
        
    def debuild(self, nodes, rtn, n):
        count = 0
        for i in range(n):
            node = nodes.pop(0)
            if node==None:
                rtn += 'null,'
                nodes.append(None); nodes.append(None);
                count += 1
            else:
                rtn += str(node.val)+','
                nodes.append(node.left); nodes.append(node.right)
        if n==count:
            return rtn[:-n*5]
        else:
            return self.debuild(nodes, rtn, n*2)
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data[1:-1]
        if len(data)==0: return None
        input = re.split(',',data)
        return self.build(input,0,0)
        
    def build(self, input, d, i):
        index = 2**d+i-1
        if index>=len(input) or input[index]=='null':
            return None
        else:
            node = TreeNode(int(input[index]))
            node.left = self.build(input, d+1, 2*i)
            node.right = self.build(input, d+1, 2*i+1)
            return node

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
