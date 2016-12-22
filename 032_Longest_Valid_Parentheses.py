class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        maxLength=0
        cStack=[]
        for i in range(0,len(s)):
            if s[i]=='(':
                cStack.append((i,s[i]))
            else:
                if len(cStack)==0 or cStack[-1][1]==')':
                    cStack.append((i,s[i]))
                else:
                    cStack.pop()
                    if len(cStack)==0:
                        maxLength=max(maxLength,i+1)
                    else:
                        maxLength=max(maxLength,i-cStack[-1][0])
        return maxLength
