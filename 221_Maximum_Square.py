class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        h = len(matrix)
        if h==0: return 0
        w = len(matrix[0])
        dp = [[0 for i in range(w+1)] for j in range(h+1)]
        rtn = 0
        
        for i,row in enumerate(matrix):
            for j,num in enumerate(row):
                if str(num)=='1':
                    dp[i+1][j+1] = min(dp[i+1][j], dp[i][j+1], dp[i][j])+1
                    rtn = max(rtn,dp[i+1][j+1])
                else:
                    dp[i+1][j+1] = 0
        return rtn**2
