class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        l1 = len(s); l2 = len(p); tbl = [];
        for i in range(l2+1):
            tbl.append([False]*(l1+1))
        
        tbl[0][0] = True
        for i in range(2,l2+1):
            tbl[i][0] = p[i-1]=='*' and tbl[i-2][0]
        
        for i in range(1,l2+1):
            for j in range(1,l1+1):
                c1 = s[j-1]; c2 = p[i-1];
                if c2=='*':
                    tbl[i][j] = tbl[i-2][j] or ((p[i-2]=='.' or p[i-2]==c1) and tbl[i][j-1])
                else:
                    tbl[i][j] = tbl[i-1][j-1] and (c1=='.' or c2=='.' or c1==c2)
                    
        return tbl[l2][l1]
