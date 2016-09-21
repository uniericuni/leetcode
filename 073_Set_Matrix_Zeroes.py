class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        
        height = len(matrix)
        length = len(matrix[0])
        isFirstRowZero = False
        isFirstColZero = False
        
        for i in range(0,length):
            if matrix[0][i] is 0:
                isFirstRowZero = True
                break
        
        for i in range(0,height):
            if matrix[i][0] is 0:
                isFirstColZero = True
                break
        
        for i in range(1,height):
            for j in range(1,length):
                if matrix[i][j] is 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                
        for i in range(1,height):
            for j in range(1,length):
                if matrix[i][0] is 0 or matrix[0][j] is 0:
                    matrix[i][j] = 0
         
        for i in range(0,length):
            if isFirstRowZero:
                matrix[0][i] = 0
        
        for i in range(0,height):
            if isFirstColZero:
                matrix[i][0] = 0
        
        return
