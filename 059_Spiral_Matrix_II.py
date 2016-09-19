class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        
        ans = []
        for i in range(1,n+1):
            ans.append([0]*n)
        print ans
        dBound = n-1
        uBound = 1
        rBound = n-1
        lBound = 0
        vAdder = 0
        hAdder = 1
        x = 0
        y = 0
        
        for i in range(1,n*n+1):
            print x, ",",  y
            ans[y][x] = i
            if x is rBound and hAdder > 0:
                rBound -= 1
                vAdder = 1
                hAdder = 0
            elif x is lBound and hAdder < 0:
                lBound += 1
                vAdder = -1
                hAdder = 0
            elif y is dBound and vAdder > 0:
                dBound -= 1
                vAdder = 0
                hAdder = -1
            elif y is uBound and vAdder < 0:
                uBound += 1
                vAdder = 0
                hAdder = 1
            
            x += hAdder
            y += vAdder
            
        return ans
            
