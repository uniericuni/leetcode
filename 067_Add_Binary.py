class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        if len(a)>len(b):
            b = '0'*(len(a)-len(b)) + b
        if len(a)<len(b):    
            a = '0'*(len(b)-len(a)) + a
        
        s = ''
        s1 = a[::-1]
        s2 = b[::-1]
        i=0; j=0
        c = 0
        while i<len(s1) and j<len(s2):
            
            if s1[i]=='1' and s2[j]=='1':
                s_t = c
                c = 1
            elif (s1[i]=='1' and s2[j]=='0') or (s1[i]=='0' and s2[j]=='1'):
                s_t = 1+c
                c = 0
            else:
                s_t = c
                c = 0
                
            if s_t>=2:
                s_t = s_t-2
                c = 1
                
            s = s+str(s_t)
            i = i+1
            j = j+1
            
        if c>=1:
            s = s+'1'
        
        return s[::-1]
            
