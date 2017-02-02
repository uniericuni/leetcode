class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stk = []
        l = str(path).split('/')
        
        for d in l:
            if d=='.' or len(d)==0:
                continue
            if d=='..': 
                if len(stk)>0:
                    stk.pop()
                continue
            stk.append(d)
        
        
        rtn = ''
        for d in stk:
            rtn = rtn+'/'+d
        if len(rtn)==0:
            rtn = '/'
        return rtn
