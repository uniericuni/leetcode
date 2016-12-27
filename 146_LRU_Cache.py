class Node:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.r=None
        self.l=None
        
class dLink:
    def __init__(self):
        self.linkList=[]
        self.head=Node(float('inf'),0)
        self.tail=Node(-float('inf'),0)
        self.head.r=self.tail
        self.tail.l=self.head
        
    def insert(self,node):
        node.r=self.tail
        node.l=self.tail.l
        self.tail.l.r=node
        self.tail.l=node
        
    def remove(self,node):
        tmp=node.l
        node.l.r=node.r
        node.r.l=tmp
        
class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.dict={}
        self.linkList=dLink()
        
    def get(self, key):
        """
        :rtype: int
        """
        if key in self.dict:
            self.linkList.remove(self.dict[key])
            self.linkList.insert(self.dict[key])
            return self.dict[key].val
        else:
            return -1
        
    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.dict:
            self.dict[key].val=value
            self.get(key)
        elif (len(self.dict)<self.capacity):
            node=Node(key,value)
            self.dict[key]=node
            self.linkList.insert(node)
        else:
            self.dict.pop(self.linkList.head.r.key)
            self.linkList.remove(self.linkList.head.r)
            node=Node(key,value)
            self.dict[key]=node
            self.linkList.insert(node)
