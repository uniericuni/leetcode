class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        maxLength=0
        cQueue=[]
        for i in range(0,len(s)):
            if s[i]=='(':
                cQueue.append((i,s[i]))
            else:
                if len(cQueue)==0 or cQueue[-1][1]==')':
                    cQueue.append((i,s[i]))
                else:
                    cQueue.pop()
                    if len(cQueue)==0:
                        maxLength=max(maxLength,i+1)
                    else:
                        maxLength=max(maxLength,i-cQueue[-1][0])
        return maxLength
