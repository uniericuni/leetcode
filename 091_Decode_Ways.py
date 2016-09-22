class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if len(s) is 0:
            return 0
            
        for c in s:
            if int(c) < int('0') or int(c) > int('9'):
                return 0
        
        return decodeJudge(s)
        
def decodeJudge(s):
    
    n = len(s)-1
    
    if int(s[0]) is int('0'):
        return 0
    
    if len(s) is 1:
        return 1
    elif len(s) is 2:
        if int(s[0]) is int('1'):
            if int(s[1]) is int('0'):
                return 1
            else:
                return 2
        elif int(s[0]) is int('2'):
            if int(s[1]) > int('0') and int(s[1]) <= int('6'):
                return 2
            else:
                return 1
        else:
            if int(s[1]) is int('0'):
                return 0
            else:
                return 1
    
    if int(s[0]) is int('1'):
        if int(s[1]) is int('0'):
            return decodeJudge(s[2:n+1])
        else:
            return decodeJudge(s[2:n+1])+decodeJudge(s[1:n+1])
    elif int(s[0]) is int('2'):
        if int(s[1]) > int('0') and int(s[1]) <= int('6'):
            return decodeJudge(s[2:n+1])+decodeJudge(s[1:n+1])
        else:
            return decodeJudge(s[2:n+1])
    else:
        if int(s[1]) is int('0'):
            return 0
        else:
            return decodeJudge(s[1:n+1])
