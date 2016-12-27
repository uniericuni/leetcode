class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        stk=[]
        rtn=0
        height.insert(0,float('inf'))
        for x,h in enumerate(height):
            stkTemp=[]
            while len(stk)>0 and h>=stk[-1][1]:
                stkTemp.append(stk.pop())
            if len(stkTemp)>0:
                bottom=stkTemp[0][1]
                for hh in stkTemp[1:]:
                    rtn+=(x-hh[0]-1)*(hh[1]-bottom)
                    bottom=hh[1]
                if len(stk)>1:
                    rtn+=(x-stk[-1][0]-1)*(h-bottom)
            stk.append((x,h))
        
        return rtn
