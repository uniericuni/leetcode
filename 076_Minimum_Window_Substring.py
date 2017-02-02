class Solution(object):
    
    def foundTest(self,dict):
        for key in dict:
            if dict[key]>0:
                return False
        return True
        
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        s=str(s)
        t=str(t)
        dict={}
        for c in t:
            if c in dict:   dict[c]=dict[c]+1
            else:           dict[c]=1
        
        i=0; j=0;
        found=False
        rtn_i=0; rtn_j=len(s)
        
        while i<=j and j<len(s):

            while not found and i<=j and j<len(s):
                c=s[j]
                if c in dict:
                    dict[c]=dict[c]-1
                found=self.foundTest(dict)
                if found:
                    break
                j=j+1
            
            while found and i<=j and j<len(s):
                c=s[i]
                if c in dict:
                    dict[c]=dict[c]+1
                found=self.foundTest(dict)
                i=i+1

            if (j-i)<(rtn_j-rtn_i):
                rtn_j=j
                rtn_i=i-1
            j=j+1
            
        if (rtn_j-rtn_i)>=len(s):
            return ''
        return s[rtn_i:rtn_j+1]
