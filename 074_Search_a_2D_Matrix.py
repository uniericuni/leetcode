class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        s = 0
        e = len(matrix)-1
        m = (s+e)/2
        while e > s:
            m = (s+e)/2
            row = matrix[m]
            if row[0] == target:
                return True
            elif row[0] > target:
                e = m-1
            elif row[0] < target:
                if e-s <= 2:
                    if matrix[e][0] > target:
                        e = m
                        s = m
                    elif matrix[e][0] == target:
                        return True
                    else:
                        s = e
                else:
                    s = m
        
                
        row = matrix[e]
        s = 0
        e = len(row)-1
        m = (s+e)/2
        while e > s:
            m = (s+e)/2
            item = row[m]
            if item == target:
                return True
            elif item > target:
                e = m-1
            else:
                s = m+1
        if row[e] == target:
            return True
        
        return False
        
