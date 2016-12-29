class Solution(object):
    
    def checkSubstring(self,word,dict,n,length):
        dictTemp=dict.copy()
        for i in range(0,n):
            v = word[i*length:(i+1)*length]
            if v in dictTemp and dictTemp[v]>0:
                dictTemp[v]-=1
            else:
                return False
        return True
        
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        
        n=len(words)
        length=len(words[0])
        word=''
        rtn=[]
        dict={}
        
        for w in words:
            if w in dict:
                dict[w]+=1
            else:
                dict[w]=1
        
        for i,c in enumerate(s):
            word+=c
            if len(word)==length*n:
                if self.checkSubstring(word,dict,n,length):
                    rtn.append(i+1-length*n)
                word=word[1:]
                
        return rtn
