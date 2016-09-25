class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        
        if not tokens:
            return 0
        
        numStack = []
        for item in tokens:
            if item == "+":
                num1 = int(numStack[len(numStack)-2])
                num2 = int(numStack[len(numStack)-1])
                numStack.pop()
                numStack.pop()
                numStack.append(str(num1+num2))
            elif item == "-":
                num1 = int(numStack[len(numStack)-2])
                num2 = int(numStack[len(numStack)-1])
                numStack.pop()
                numStack.pop()
                numStack.append(str(num1-num2))
            elif item == "*":
                num1 = int(numStack[len(numStack)-2])
                num2 = int(numStack[len(numStack)-1])
                numStack.pop()
                numStack.pop()
                numStack.append(str(num1*num2))
            elif item == "/":
                num1 = int(numStack[len(numStack)-2])
                num2 = int(numStack[len(numStack)-1])
                numStack.pop()
                numStack.pop()
                num = abs(num1)/abs(num2)
                if num1*num2 < 0:
                    num *= -1
                numStack.append(str(num))
            else:
                numStack.append(item)
            print numStack[len(numStack)-1]
            
                
        return int(numStack[0])
