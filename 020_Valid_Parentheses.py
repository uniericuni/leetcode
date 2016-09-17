class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        e = ''
        list = []
        for c in s:
            if c=='(' or c=='[' or c=='{':
                list.append(c)
            elif c==')' or c==']' or c=='}':
                if not list:
                    return False
                e = list.pop()
                if e=='(' and c==')':
                    continue
                elif e=='[' and c==']':
                    continue
                elif e=='{' and c=='}':
                    continue
                else:
                    return False
        
        if not list:
            return True
        else:
            return False
