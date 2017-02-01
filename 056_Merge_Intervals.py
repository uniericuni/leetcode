# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insertInterval(self, rtn, l):
        if (len(rtn)>0) and (rtn[-1].end >= l.start):
            prev = rtn.pop()
            new = Interval(s=prev.start, e=max(prev.end, l.end))
            rtn.append(new)
        else:
            rtn.append(l)
    
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        
        n = len(intervals)/2
        if n==0:
            return intervals
            
        l1 = self.merge(intervals[:n])
        l2 = self.merge(intervals[n:])
        rtn = []
        i1 = 0
        i2 = 0
        
        while len(l1)>i1 and len(l2)>i2:
            if l1[i1].start < l2[i2].start:
                self.insertInterval(rtn, l1[i1])
                i1 += 1
            else:
                self.insertInterval(rtn, l2[i2])
                i2 += 1
        while len(l1)>i1:
            self.insertInterval(rtn, l1[i1])
            i1 += 1
        while len(l2)>i2:
            self.insertInterval(rtn, l2[i2])
            i2 += 1
            
        return rtn
        
