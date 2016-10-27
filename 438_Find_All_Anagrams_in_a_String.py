import itertools

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        
        rtn = []
        N = len(s)
        n = len(p)
        list = ["".join(perm) for perm in itertools.permutations(p)]
        for i,c in enumerate(s):
            if i+n > N:
                break
            if s[i:i+n] in list:
                rtn.append(i)
                
        return rtn
            
