# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
import heapq as hq

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        intervals = sorted(intervals, key=lambda x:x.start)
        q=[]; rtn=0;
        for i in intervals:
            while len(q)!=0 and hq.nsmallest(1,q)[0]<=i.start:
                hq.heappop(q)
            hq.heappush(q,i.end)
            rtn = max(rtn,len(q))
        return rtn
