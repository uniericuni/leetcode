class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix[0])
        n = len(matrix)
        i = 0
        j = n-1
        while i<m and j>=0:
            if matrix[j][i] == target: return True
            if matrix[j][i] > target: j-=1
            else: i+=1
        return False
