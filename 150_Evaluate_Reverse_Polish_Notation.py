class Solution(object):
    def process(self,s1,s2,s3):
        if s3=="+":
            return int(s1)+int(s2)
        elif s3=="-":
            return int(s1)-int(s2)
        elif s3=="*":
            return int(s1)*int(s2)
        elif s3=="/":
            return int(float(s1)/float(s2))
    
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        
        tokenStack = []
        for token in tokens:
            tokenStack.append(token)
            if token=="+" or token=="-" or token=="*" or token=="/":
                rtn=self.process(tokenQueue[-3],tokenQueue[-2],tokenQueue[-1])
                tokenStack.pop()
                tokenStack.pop()
                tokenStack.pop()
                tokenStack.append(rtn)
                
        return int(tokenStack[0])
