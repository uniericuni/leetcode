# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def find(self,s,e):
        if s==e:
            return s
        if isBadVersion((s+e)/2):
            return self.find(s,(s+e)/2)
        else:
            return self.find((s+e)/2+1,e)
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.find(1,n)
        
