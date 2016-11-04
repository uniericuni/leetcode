import itertools

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
        rtn = ""
        n = len(s)
        step = numRows*2-2
        
        if step<=0 or n<=numRows:
            return s
        
        for i in range(0,numRows):
            if i==0 or i==numRows-1:    
                rtn += s[i:n:step]
            else:                      
                new1 = s[i:n:step]
                new2 = s[step-i:n:step]
                zips = itertools.izip_longest(new1,new2, fillvalue='')
                rtn += ''.join(itertools.chain.from_iterable(zips))
                
        return rtn
