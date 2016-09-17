class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        n = len(s)
        i = 0
        j = 0
        ans = 0
        tbl = {}
        
        for element in range(1,128):
            tbl[element] = None
            
        while i<n and j<n:
            k = ord(s[j])
            if tbl[k] is not None:
                if i<=tbl[k]:
                    i = tbl[k]+1
            tbl[k] = j
            ans = max(j-i+1, ans)
            j += 1
                
        return ans
