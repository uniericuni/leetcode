class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        cut = []
        for i in range(0,len(s)+1):
            cut.append(i-1)
        for i in range(1,len(s)+1):
            j = 0
            while i-j>0 and i+j<=len(s) and s[i-j-1]==s[i+j-1]:
                cut[i+j] = min(cut[i-j-1]+1,cut[i+j])
                j += 1
            j = 0
            while i-j-1>0 and i+j<=len(s) and s[i-j-2]==s[i+j-1]:
                cut[i+j] = min(cut[i-j-2]+1,cut[i+j])
                j += 1
                
            
        return cut[len(s)]
