class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        l = str(x)
        if l[0]=='-':  rtn = int(l[0] + l[:0:-1])
        else:          rtn = int(l[::-1])
        if rtn>2147483646 or rtn<-2147483647: return 0
        else: return rtn
