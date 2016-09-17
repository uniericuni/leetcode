class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        ans = 0
        i = 0
        j = len(height)-1
        
        while j > i:
            area = (j-i) * min(height[i], height[j])
            ans = max(area, ans)
            if(height[i]<height[j]):
                i += 1
                
            else:
                j -= 1
                
        return ans
