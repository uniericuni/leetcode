# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        
        intervals.sort(key=lambda x: x.start)
        s = newInterval.start
        e = newInterval.end
        isInsert = False
        i = 0
        rtn = []
        
        for l in intervals:
            
            if isInsert:
                rtn.append(l)
            elif l.start>e:
                rtn.append(newInterval)
                rtn.append(l)
                isInsert = True
            elif l.end>=s:
                s = min(s,l.start)
                e = max(e,l.end)
                newInterval.start = s
                newInterval.end = e
            else:
                rtn.append(l)
                
        if not isInsert:
            rtn.append(newInterval)
                
        return rtn
