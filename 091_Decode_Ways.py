class Solution(object):
    
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==0 or ord(s[0])<ord('1') or ord(s[0])>ord('9'):
            return 0
        dp=[0]*(len(s)+1)
        dp[0]=1; dp[1]=1;
        for i in range(1,len(s)):
            if not s[i].isdigit():
                return 0
            if int(s[i-1:i+1])<=26 and int(s[i-1:i+1])>9: dp[i+1]=dp[i+1]+dp[i-1]
            if s[i]!='0': dp[i+1]=dp[i+1]+dp[i]
        return dp[-1]
