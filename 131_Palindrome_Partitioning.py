class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        
        rtn = []
        l = []
        dfs(rtn, s, l)
        
        return rtn

def dfs(rtn, s, l):
    if len(s) == 0:
        rtn.append(l)
    else:
        for i in range(0,len(s)):
            if palindrome(s[:i+1]):
                lt = l[:]
                lt.append(s[:i+1])
                dfs(rtn, s[i+1:], lt[:])

def palindrome(s):
    it = 0
    while it < len(s)/2:
        if s[it] != s[len(s)-it-1]:
            return False
        it+=1
    return True
