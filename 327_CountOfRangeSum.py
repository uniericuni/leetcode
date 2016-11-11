import numpy as np

class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        nums.insert(0,0)
        csum = np.cumsum(nums).tolist()
        csum2 = csum[:]
        rtn = self.count(csum, 0, len(csum)-1, upper)
        rtn -= self.count(csum2, 0, len(csum)-1, lower-1)
        return rtn
    
    # divine and conquer    
    def count(self, csum, lo, hi, upper):
        if lo>=hi: return 0
        m = (lo+hi)//2
        rtn = self.count(csum, lo, m, upper)
        rtn += self.count(csum, m+1, hi, upper)
        rtn += self.countPairs(csum, lo, hi, m, upper)
        self.merge(csum, lo, hi, m)
        return rtn

    # double pointers        
    def countPairs(self, csum, lo, hi, m, upper):
        rtn = 0
        for i in range(lo, m+1):
            j = m+1
            while j<=hi and csum[j]-csum[i]<=upper: j+=1
            rtn += j-m-1
        return rtn
        
    # merge sort
    def merge(self, csum, lo, hi, m):
        rtn = []
        i = lo
        j = m+1
        while i<=m and j<=hi:
            if csum[j]<=csum[i]:
                rtn.append(csum[j])
                j+=1
            else:
                rtn.append(csum[i])
                i+=1
        if i>m: rtn.extend(csum[j:hi+1])
        else:  rtn.extend(csum[i:m+1])
        for i in range(lo, hi+1):
            csum[i] = rtn[i-lo]
