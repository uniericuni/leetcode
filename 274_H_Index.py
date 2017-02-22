class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        tbl = [0]*(n+1); index = n; i=n-1
        for c in citations:
            if c>n:
                tbl[-1]+=1
            else:
                tbl[c]+=1
        tbl.reverse();
        print tbl
        h = 0;
        for i,c in enumerate(tbl):
            h += c
            if h >= n-i:
                return n-i
        return 0
