class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        
        heights.insert(0,-1)
        heights.append(-1)
        rtn=0
        stk=[]
        for i,h in enumerate(heights):
            while len(stk)>0 and heights[stk[-1]]>h:
                s=stk.pop()
                if h<heights[s]:
                    rtn=max(rtn,(i-stk[-1]-1)*heights[s])
            stk.append(i)
            
        return rtn
