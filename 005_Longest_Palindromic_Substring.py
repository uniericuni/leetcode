class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return ""

        s = '$'+'$'.join(s)+'$'
        dict = [0]*len(s)
        max_ind = 0
        max_size = 0
        
        
        for i,c in enumerate(s):
            j = 0
            while i-j-1>=0 and i+j+1<len(s):
                if s[i-j-1]!=s[i+j+1]:  break
                else:                   j += 1
                if i-j+dict[i-j] >= i:  
                    if i-2*j-dict[i-2*j] < i-j-dict[i-j]:   j = dict[i-j]-j
                    elif i-2*j-dict[i-2*j] > i-j-dict[i-j]: j = dict[i-2*j]
                    else:                                   j = max(j,dict[i-2*j])
            dict[i] = j
            if max_size<j:
                max_size = j
                max_ind = i
            
        return s[max_ind-max_size:max_ind+max_size+1].replace('$','')
