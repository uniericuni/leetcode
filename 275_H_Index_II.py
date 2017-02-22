class Solution(object):
    def search(self, citations, n, s, e):
        k = (s+e)/2
        h = n-k-1
        if s==e or (citations[k]<=h and citations[k+1]>=h):
            return h
        elif citations[k]>h:
            return self.search(citations, n, s, k-1)
        else:
            return self.search(citations, n, k+1, e)
        
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        if n==0: return 0
        n+=1
        citations.insert(0,0)
        return self.search(citations, n, 0, n-1)
